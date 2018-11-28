#include <iostream>
#include <string>
using namespace std;

string dictionary[5001];


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int L,D,N;
    cin >> L >> D >> N;
    for(int i=0;i<D;++i)
        cin >> dictionary[i];
    for(int i=1;i<=N;++i)
    {
        string token[16];
        char ch;
        int j=0;
        getchar();
        while(j!=L)
        {
            if((ch=getchar())=='(')
            {
                while((ch=getchar())!=')')
                    token[j]+=ch;
            }
            else
                token[j]=ch;
            ++j;
        }
        int count =0;
        for(int j=0;j<D;++j)
        {
            bool flag=1;
            for(size_t k=0;k<dictionary[j].size();++k)
            {
                if(token[k].find(dictionary[j][k])==string::npos)
                {
                    flag=0;
                    break;
                }
            }
            if(flag==1)
                ++count;
        }
        cout << "Case #" << i << ": " << count << endl;
    }
	return 0;
}