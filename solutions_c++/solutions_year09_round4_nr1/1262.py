#include <vector>
#include <string>
#include <iostream>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <fstream>

using namespace std;


#define All(v) (v).begin(), (v).end()
#define ffor(i,n) for(int i=0; i<n; i++)
#define LL long long
#define LD long double
#define psh push_back
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))



int bubbleSort(vector<int> &array, int size)
 {
int cnt = 0;
    int swapped;
    int i;
    for (i = 1; i < size; i++)
    {
        swapped = 0;    //this flag is to check if the array is already sorted
        int j;
        for(j = 0; j < size - i; j++)
        {
            if(array[j] > array[j+1])
            {
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
                swapped = 1;
cnt++;
            }
        }
        if(!swapped){
            break; //if it is sorted then stop
        }
    }
return cnt;

 }

int correct(vector<int> &vec)
{
	for(int j = vec.size()-1; j >= 0; j--)
	{
		if(j+1 < vec[j])
			return j;
	}
	return -1;
}

int main()
{
	int c;
	cin >> c;

	for(int i = 0; i < c; i++)
	{
		int n;
		cin >> n;

		vector<int> vals,cp,srt;

		ffor(j,n)
		{
			int last	= 0;
			ffor(k,n)
			{
				char t;
				cin >> t;
				if(t == '1')
					last = k+1;
			}
			vals.psh(last);
		}

		cp	= vals;
		int r;
		int cnt	= 0;
		while((r = correct(vals)) != -1)
		{

			int t	= vals[r];

			int b = r+1;
			while(vals[b] >= vals[r])
			{
				b++;
				cnt++;
			}

			vals[r] = vals[b];
			vals[b]	= t;
			cnt++;
			//ffor(k,vals.size())
			//	cout << vals[k];
			//cout << endl;
		}


		ffor(j,vals.size())
			srt.psh(-1);

		ffor(j,vals.size())
		{
			ffor(k,cp.size())
				if(cp[k] == vals[j])
				{
					srt[k] = j;
					cp[k] = -1;
					break;
				}
		}

		cout << "Case #" << i+1 << ": " <<  bubbleSort(srt,srt.size()) <<    endl;
	}
}
