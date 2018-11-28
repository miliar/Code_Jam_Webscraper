#include <stdio.h>
#include <new.h>
#include <string.h>

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

class CAlienDict
{
	CAlienDict(const CAlienDict&);
	CAlienDict& operator=(const CAlienDict&);
private:
	scoped_array< scoped_array<char> > dict;
	int word_len;
	int words_num;
public:
	CAlienDict() { ; }
	~CAlienDict() { ; }
public:
	bool input(int len,int num)
	{
		words_num = num;word_len = len;
		dict.init(words_num);
		for(int i = 0;i < words_num;i ++)
		{
			dict[i].init(word_len+1);
			scanf("%s",dict[i].pointer());
		}
		return true;
	}
public:
	int count(const char* buffer)
	{
		int ret = 0;
		for(int i = 0;i < words_num;i ++)
		{
			ret += match(buffer,dict[i].data());
		}
		return ret;
	}
private:
	bool match(const char* buffer,const char* pat)
	{
		int p = 0,len = strlen(buffer);
		for(int k = 0;k < len && p < word_len;k ++)
		{
			char ch = buffer[k];
			if(ch == '(')
			{
				for(++ k;')' != buffer[k] && buffer[k] != pat[p];++ k);
				if(')' == buffer[k]) return false;
				for(++ k;')' != buffer[k];++ k);
				p ++;
			}
			else
			{
				if(ch != pat[p]) return false;
				p ++;
			}
		}
		return (p == word_len) && (k == len);
	}
};

int main()
{	
	int word_len = 0,words_num = 0;
	int nCases = 0;
	scanf("%d%d%d",&word_len,&words_num,&nCases);
	CAlienDict dict;dict.input(word_len,words_num);
	const int max_len = 600;
	char buffer[max_len];
	for(int iCases = 1;iCases <= nCases;iCases ++)
	{
		scanf("%s",buffer);
		printf("Case #%d: %d\n",iCases,dict.count(buffer));
	}
	return 0;
}
