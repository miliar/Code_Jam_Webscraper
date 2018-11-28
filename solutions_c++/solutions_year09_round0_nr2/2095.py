#include <iostream>


char letter(int i) {return (char) ('a'-1+i); }

struct Data
{
	size_t height, component;
};


struct Map
{
	Data *data;
	int rows, cols;
	int max;
	size_t totalC;

	Map(size_t r, size_t c) :
		rows(r), cols(c), totalC(0)
	{
		data = new Data[r*c];
		for(size_t i = 0; i < r*c; ++i)
		{
			std::cin >> data[i].height;
			data[i].component = 0;	
		}
	}

	void collapse(int x, int y)
	{
		if (x == y) return;
		totalC =0;
		if (y < x) { int tmp = y; y = x; x = tmp; }
		for(size_t i = 0; i < rows*cols; ++i) {
			if (data[i].component == y) data[i].component =x;
			if (data[i].component > y) data[i].component--;
			if (data[i].component > totalC) totalC= data[i].component;
		}
	}

	~Map()
	{
		delete[] data;
	}

	size_t getH(size_t r, size_t c) const { return data[cols*r+c].height; }
	size_t getC(size_t r, size_t c) const { return data[cols*r+c].component; }
	Data* get(size_t r, size_t c) { return &data[cols*r+c]; }
	
	Data* getMin(size_t r, size_t c)
	{
		Data *res = get(r,c);
		if (r > 0 && getH(r-1,c) < res->height) res = get(r-1,c);
		if (c > 0 && getH(r,c-1) < res->height) res = get(r,c-1);
		if (c+1 < cols && getH(r,c+1) < res->height) res = get(r,c+1);
		if (r+1 < rows && getH(r+1,c) < res->height) res = get(r+1,c);
		if (res == get(r,c)) res = 0;
		return res;
	}

	void process()
	{
		totalC= 0;
		get(0,0)->component = ++totalC;
		for(size_t r = 0; r < rows; r++)
		{
			for (size_t c = 0; c < cols; c++)
			{
				Data *d = get(r,c);
				Data *min = getMin(r,c);
				
				if (!min)
				{
					// a sink
					if (!d->component) d->component = ++totalC;
					continue;
				}

				if (!min->component) min->component = ++totalC;

				if (d->component)
				{
					collapse(min->component, d->component);
				}
				else d->component = min->component;
			}
		}


	}

	void show() const
	{
		for(size_t r = 0; r < rows; ++r)
		{
			for(size_t c = 0; c < cols; ++c)
			{
				std::cout << letter(getC(r,c));
				//std::cout << getH(r,c);
				if (c+1 < cols) std::cout << " ";
			}
			std::cout << std::endl;
		}
	}
};


int main(size_t argc, char **argv)
{

	size_t N = 0; 
	std::cin >> N;
	for(size_t i = 0; i < N; i++)
	{
		size_t r,c;
		std::cin >> r >> c;
		Map m(r,c);
		std::cout << "Case #" << i+1 <<":" <<std::endl;
		m.process();
		m.show();
	}
	return 0;
}
