#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
    char engine[100][101],query[1000][101];
    char temp[100];
    int num,casenum,i,k,max,s,q,result,pos;
    cin.getline(temp,100);
    num=atoi(temp);
    for(casenum=1;casenum<=num;casenum++)
    {
        cin.getline(temp,100);
        s=atoi(temp);
        for(i=0;i<s;i++)
        {
            cin.getline(engine[i],101);
        }
        cin.getline(temp,100);
        q=atoi(temp);
        for(i=0;i<q;i++)
        {
            cin.getline(query[i],101);
        }

        for(result=0,pos=0;pos<q;)
        {
            for(max=pos,i=0;i<s;i++)
            {
                for(k=pos;k<q&&strcmp(engine[i],query[k]);k++);
                if(k>max)
                {
                    max=k;
                }
            }
            pos=max;
            result++;
        }
        result--;
	if(result<0)
		result=0;
        cout<<"Case #"<<casenum<<": "<<result<<endl;
        /**
        cout<<s<<" "<<q<<endl;
        for(i=0;i<s;i++)
        {
            cout<<engine[i]<<endl;
        }
        for(i=0;i<q;i++)
        {
            cout<<query[i]<<endl;
        }
        **/
    }
    return 0;
}
