#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DEBUG
#define REP(i,a) for(i=0;i<a;i++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define VE vector<int>
#define SZ size()
#define PB push_back
#define all(i) (i).begin(), (i).end()

int main()
{
/*
   freopen("inputC.txt","r",stdin);
   freopen("outputC.txt","w",stdout);
*/
    int test,i,a,b,j,k,l,number,cnt;
    scanf("%d",&test);
    REP(l,test)
    {
        scanf("%d %d",&a,&b);
        vector <bool> band;
        band.assign(b+2,false);

        char buff[10],aux[10],cp[10];
        cnt=0;
        FOR(i,a,b+1)
        {
            //cout<<"number:"<<i<<endl;
            sprintf(buff,"%d",i);
            FOR(k,1,strlen(buff))
            {
                REP(j,k)
                {
                    aux[j]=buff[strlen(buff)-(k)+j];
                }
                aux[j]='\0';
                //cout<<"->"<<aux<<endl;
                strcat(aux,buff);
                aux[strlen(buff)]='\0';
                //cout<<aux<<endl;
                sscanf(aux,"%d",&number);
                //cout<<number<<endl;
                if(band[number]==false && number>=a && b>=number && i!=number)
                {
                    cnt++;
                    //cout<<"resp:"<<i<<" + "<<number<<endl;
                    //band[number]=true;
                    band[i]=true;
                }
            }
        }
        printf("Case #%d: %d\n",l+1,cnt);
    }
/*
    fclose(stdin);
	fclose(stdout);
*/
   return 0;
}
