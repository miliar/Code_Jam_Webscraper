#include <stdio.h>
#include <new>

template <class _T1, class _T2>
inline void construct_n(_T1 * p,const _T2 & v,size_t n) { for(_T1* end = p + n;p != end; new (p++) _T1(v)); }

template <class elem_t>
class scoped_array
{
private:
	scoped_array(const scoped_array&);
	scoped_array& operator= (const scoped_array&);
private:
	elem_t* _data;
	size_t _size;
public:
	scoped_array():_data(NULL),_size(0) { ; }
	~scoped_array() { clear(); }
public:
	bool init(size_t size) { if(0 == size) return false;clear();_data = new elem_t[size];if(NULL == _data) return false;_size = size;return true; }
	bool init(size_t size,const elem_t& e) { if(init(size)) { construct_n(_data,e,size);return true; };return false; }
	void clear() { if(NULL != _data) delete[] _data;_data = NULL;_size = 0; }
public:
	elem_t& operator[](size_t index) { return _data[index]; }
	const elem_t& operator[](size_t index)const { return _data[index]; }
public:
	const elem_t* data()const { return _data; }
	elem_t* pointer() { return _data; }
public:
	size_t size() const { return _size;	}
};

class CRootedTree
{
	CRootedTree(const CRootedTree&);
	CRootedTree& operator=(const CRootedTree&);
public:
	enum { kInvalid = (size_t)(-1), };
protected:
	scoped_array<size_t> _data;
	size_t _size;
public:
	CRootedTree() { ; }
	~CRootedTree() {  }
public:
	bool init(size_t size) { _size = size;return _data.init(size,kInvalid); }
public:
	bool link(size_t son,size_t parent)
	{
		if(son >= _size || parent >= _size) return false;
		if(parent == _data[son]) return true;
		if(kInvalid != _data[son]) return false;
		_data[son] = parent;
		return true;
	}
	size_t root(size_t idx)
	{
		for(;idx < _size && _data[idx] != kInvalid;idx = _data[idx]);
		return idx < _size?idx:kInvalid;
	}
public:
	size_t count()
	{
		size_t ret = 0;
		for(size_t i = 0;i < _size;i ++) { ret += (_data[i] == kInvalid); }
		return ret;
	}
	size_t lca(size_t first,size_t second)
	{
		if(first >= _size || second >= _size) return (size_t)(-1);
		int *trace = new int[_size];for(size_t i = 0;i < _size;i ++) { trace[i] = 0; }
		size_t ret = first;
		for(;ret != kInvalid;ret = _data[ret]) { trace[ret] = 1; }
		for(ret = second;ret != kInvalid && !trace[ret];ret = _data[ret]);
		return ret;
	}
};

class CUnionFindSet:public CRootedTree
{
	CUnionFindSet(const CUnionFindSet&);
	CUnionFindSet& operator=(const CUnionFindSet&);
private:
	typedef CRootedTree base;
private:
	scoped_array<size_t> _rank;
public:
	CUnionFindSet() { ; }
	~CUnionFindSet() { ; }
public:
	bool init(size_t size)
	{
		if(!base::init(size)) return false;
		return _rank.init(size,0);
	}
public:
	bool merge(size_t a,size_t b) 
	{
		size_t root1 = find(a);
		size_t root2 = find(b);
		if(base::kInvalid == root1 || base::kInvalid == root2) return false;
		if(root1 == root2) return true;
		if(_rank[root1] > _rank[root2]) _data[root2] = root1;
		else _data[root1] = root2;
		if(_rank[root1] == _data[root2]) _rank[root2] ++;
		return true;
	}
	bool diff(size_t a,size_t b)
	{
		size_t root1 = find(a);
		size_t root2 = find(b);
		return root1 != root2;
	}
public:
	size_t find(size_t a)
	{
		if(a >= _size) return base::kInvalid;
		if(_data[a] == base::kInvalid) return a;
		_data[a] = find(_data[a]);
		return _data[a];
	}
};

class CAltitudeMap
{
	CAltitudeMap(const CAltitudeMap&);
	CAltitudeMap& operator=(const CAltitudeMap&);
private:
	enum { kInvalid = 20000, };
private:
	int height;
	int width;
public:
	scoped_array< scoped_array<int> > altitudes;
	CUnionFindSet finder;
public:
	CAltitudeMap() { ; }
	~CAltitudeMap() { ; }
public:
	bool input()
	{
		scanf("%d %d",&height,&width);
		finder.init(height*width);
		altitudes.init(height);
		for(int i = 0;i < height;i ++)
		{
			altitudes[i].init(width);
			for(int k = 0;k < width;k ++) scanf("%d",&altitudes[i][k]);
		}
		return true;
	}
public:
	bool doit()
	{
		for(int i = 0;i < height;i ++)
		{
			for(int k = 0;k < width;k ++)
			{
				finder.merge(_get_direct(i,k),i*width+k);
			}
		}
		return true;
	}
public:
	bool output()
	{
		char ch = 'a';
		scoped_array<char> resp;resp.init(height*width,' ');
		for(int i = 0;i < height;i ++)
		{
			for(int k = 0;k < width;k ++)
			{
				int idx = finder.find(i*width + k);
				if(' ' == resp[idx]) resp[idx] = ch ++;
				printf("%c%c",resp[idx],((k + 1 == width)?'\n':' '));
			}
		}
		return true;
	}
private:
	int _get_altitude(int x,int y)
	{
		if(x < 0 || x >= height) return kInvalid;
		if(y < 0 || y >= width) return kInvalid;
		return altitudes[x][y];
	}
	int _get_direct(int x,int y)
	{
		int min_x = x,min_y = y;
		int min_val = _get_altitude(x,y);
		int val = _get_altitude(x - 1,y);
		if(val < min_val) { min_x = x - 1;min_y = y;min_val = val; }
		val = _get_altitude(x,y-1);
		if(val < min_val) { min_x = x;min_y = y - 1;min_val = val; }
		val = _get_altitude(x,y+1);
		if(val < min_val) { min_x = x;min_y = y + 1;min_val = val; }
		val = _get_altitude(x+1,y);
		if(val < min_val) { min_x = x + 1;min_y = y;min_val = val; }
		return min_x*width + min_y;
	}
};

int main()
{
	int nCases = 0;
	scanf("%d",&nCases);
	CAltitudeMap obj;
	for(int iCases = 1;iCases <= nCases;iCases ++)
	{
		obj.input();
		obj.doit();
		printf("Case #%d:\n",iCases);
		obj.output();
	}
	return 0;
}
