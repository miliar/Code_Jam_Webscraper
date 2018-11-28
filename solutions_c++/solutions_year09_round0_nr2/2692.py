#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct data
{
	int key;
	int val;
	vector<int> children;
	char ch;
} data_t;

typedef struct {
	int min;
	int least;
} minkey_t;

bool operator<(const minkey_t & lh, const minkey_t & rh)
{
	return lh.least < rh.least;
}

int minimum(data_t **data, int ind)
{
	int min = ind;
	for(int c = 0; c < (int)(*data)[ind].children.size(); c++)
	{
		int temp = minimum(data, (*data)[ind].children[c]);
		if(temp < min) min = temp;
	}
	return min;
}

void traverse(data_t **data, int ind)
{
	for(int c = 0; c < (int)(*data)[ind].children.size(); c++)
	{
		if((*data)[(*data)[ind].children[c]].ch == 'a'-1) 
			(*data)[(*data)[ind].children[c]].ch = (*data)[ind].ch;
		traverse(data, (*data)[ind].children[c]);
	}
}

int main()
{
	int T;
	int X, Y;
	ifstream in("B-large-attempt0.in");
	ofstream out("B-large-attempt0.out");

	in >> T;
	for(int i = 0; i < T; i++)
	{
		// Each test
		char globalch = 'a' - 1;
		
		data_t *data;
		minkey_t *minkeys = new minkey_t[27];
	
		in >> X >> Y;
		data = new data_t[X*Y];
		
		for(int x = 0; x < X; x++)
			for(int y = 0; y < Y; y++) {
				in >> data[x*Y + y].val;
				data[x*Y + y].key = x*Y + y;
				data[x*Y + y].ch = globalch;
			}
			
		int min = -1, minnum = 0;
		for(int x = 0; x < X; x++)
			for(int y = 0; y < Y; y++)
			{
				// For each point check neighbors
				int px[4] = {-1,0,1,0}, py[4] = {0,-1,0,1};
				for(int k = 0; k < 4; k++){px[k]+=x;py[k]+=y;}
				min = -1;
				for(int k = 0; k < 4; k++)
				{
					if( px[k] < 0 || px[k] > X-1 || py[k] < 0 || py[k] > Y-1) continue;
					if(data[x*Y+y].val > data[px[k]*Y+py[k]].val) {
						if(min == -1) min = px[k]*Y+py[k];
						else if(data[min].val > data[px[k]*Y+py[k]].val || (data[min].val == data[px[k]*Y+py[k]].val && (data[min].key > data[px[k]*Y+py[k]].key)))
							min = px[k]*Y+py[k];
					}
				}
				if (min != -1) {
					data[min].children.push_back(x*Y+y);
				}else{
					minnum ++;
					minkeys[minnum-1].min = x*Y+y;
					minkeys[minnum-1].least = 0;
				}
			}
			
		for(int d = 0; d < minnum; d++)
			minkeys[d].least = minimum(&data, minkeys[d].min);
		
		sort(minkeys, minkeys + minnum);
		
		for(int d = 0; d < minnum; d++)
		{
			globalch++;
			data[minkeys[d].min].ch = globalch;
		}
		
		for(int d = 0; d < minnum; d++)
			traverse(&data, minkeys[d].min);
		
		out << "Case #" << i+1 << ":"<< endl;
		for(int x = 0; x < X; x++) {
			for(int y = 0; y < Y; y++)
				out << data[x*Y+y].ch << " ";
			out << endl;
		}
		
		delete[] minkeys;
		delete[] data;
	}
	
}