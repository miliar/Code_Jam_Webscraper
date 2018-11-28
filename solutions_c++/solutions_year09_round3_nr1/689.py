#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <set>
using namespace std;
int main()
{
    freopen("r32.in","r",stdin);
    freopen("r32.out","w",stdout);
    int i,j,alp,xyz;
	unsigned long long int mul,res,no,ind,x23[30];
    char c,s[65];
	int cnt,cnt1 = 500;
   
    vector <unsigned long long int> v1;
    vector <char> v;
    vector <char>::iterator it;
    scanf("%lld%c",&no,&c);
    for(int i=1;i<=no;i++)
    {
        gets(s);
        
            for(int j=0;j<strlen(s);j++)
            {
                if(find(v.begin(),v.end(),s[j])==v.end())
                {
                    v.push_back(s[j]);
                }
            }
            if(v.size()>1)
        {
            c=v[0];
            v[0]=v[1];
            v[1]=c;
            for(int j=0;j<strlen(s);j++)
            {
                it=find(v.begin(),v.end(),s[j]);
                ind=it-v.begin();
                v1.push_back(ind);

            }
			for( alp = 0;alp <cnt1;alp++)
			cnt++;
					
		   res=0;mul=1;
            for(int j=v1.size()-1;j>=0;j--)
            {
                res+=(v1[j]*mul);
                mul*=v.size();
            }
            printf("Case #%d: %lld\n",i,res);
        }
        else
        {
                if(strlen(s)==1)
                    printf("Case #%d: %d\n",i,1);
                else
                {
                     res=0;mul=1;
                     for(int j=0;j<strlen(s);j++)
                         v1.push_back(1);
                    for(int j=v1.size()-1;j>=0;j--)
                    {
                        res+=(v1[j]*mul);
                        mul*=2;
                    }
                    printf("Case #%d: %lld\n",i,res);
               }

        }
        v.erase(v.begin(),v.end());
        v1.erase(v1.begin(),v1.end());
    }
}
