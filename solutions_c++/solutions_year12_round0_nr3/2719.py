#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

char in_file[] = "C-large.in";
char out_file[] = "C-large.out";

int get_all_z(int a, int b)
{
    int len = 0;
    int i,j,k;
    int left, begin,end,right;
    int num,rnum;
    int worker = a;
    vector<int> temp;
    vector<vector<int> > mapper;

    //几位数
    while(worker != 0)
    {
        len++;
        worker /= 10;
    }

    for (i=a; i<=b; i++)
    {
        for (j=1; j<len; j++)
        {
            
            left = i / (int)pow((double)10, (int)j);
            right = i % (int)pow((double)10,(int)j);
            rnum = right * (int)pow((double)10,(int)(len-j)) + left;

            if (rnum >= a && rnum <= b && rnum != i)
            {
                temp.clear();
                temp.push_back(i);
                temp.push_back(rnum);
                sort(temp.begin(),temp.end());
                mapper.push_back(temp);
            }
        }
    }

    sort(mapper.begin(), mapper.end());
    vector<vector<int> >::iterator iter = unique(mapper.begin(), mapper.end());
    mapper.erase(iter, mapper.end());
    return mapper.size();
}


int main()
{
    int case_count;
    int t;
    int ret;
    int a, b;

    freopen(in_file, "r", stdin);
    freopen(out_file,"w", stdout);

    cin >> case_count;

    for (t=1;t<=case_count;t++)
    {
        cin >> a >> b;

        ret = get_all_z(a, b);
        cout << "Case #" << t << ": " << ret << endl;
    }

	return 0;    
}
