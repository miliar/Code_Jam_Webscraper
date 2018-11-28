#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<map>
#include<stack>
#include<queue>
#define max(a,b)(a>b?a:b)
#define min(a,b)(a<b?a:b)
#define inf 100
#include<conio.h>


using namespace std;

int M,N,P;
int mat[512][512];
map<int,int>mp;

void color(int ii,int jj,int val);
int Find_max(int ii,int jj,int v);


string BaseConversion(string xstr,int xbase,int ybase)
{
    string str="0123456789ABCDEF";
    long long store[128],i,multi,sum;
    string ystr;

    for(i=sum=0;i<str.size();i++)
        store[str[i]]=i;
    multi=1;
    for(i=xstr.size()-1;i>=0;i--)
    {
        sum+=(store[xstr[i]]*multi);
        multi*=xbase;
    }
    while(true)
    {
        ystr.push_back(str[sum%ybase]);
        sum/=ybase;
        if(sum==0)
            break;
    }

    for(i=ystr.size();i<N;i++)
        ystr.push_back('0');
    reverse(ystr.begin(),ystr.end());
    return ystr;
}



int main()
{
    freopen("c-small.in","r",stdin);
    freopen("c-small.out","w",stdout);

    int test,i,j,total,_max,val,ind_i,ind_j,_case=1;
    string str,in;
    vector<int>res;

    scanf("%d",&test);
    while(test--)
    {
        res.clear();
        memset(mat,0,sizeof(mat));
        scanf("%d %d",&M,&N);
        getchar();
        for(i=0;i<M;i++)
        {
            cin>>in;
            str=BaseConversion(in,16,2);
            //cout<<str<<endl;
            //getch();
            for(j=0;j<str.size();j++)
                if(str[j]=='0')
                    mat[i][j]=0;
                else mat[i][j]=1;//end of processing input;
        }
        /*for(i=0;i<M;i++){
            for(j=0;j<N;j++)
                printf("%d ",mat[i][j]);
            printf("\n");
        }*/

        total=0;
        mp.clear();
        while(1)
        {
            _max=0;
            for(i=0;i<M;i++)
                for(j=0;j<N;j++)
                {
                    if(mat[i][j]!=-1)
                    {
                        val=Find_max(i,j,1);
                        if(val>_max)
                        {
                            _max=val;
                            ind_i=i;
                            ind_j=j;
                        }
                    }
                }
            if(_max==0)
                break;
            if(!mp[_max]){
                res.push_back(_max);
                total++;
            }
            mp[_max]++;
            color(ind_i,ind_j,_max);
            /*printf("ind_i=%d,ind_j=%d,_max=%d\n",ind_i,ind_j,_max);
            for(i=0;i<M;i++){
                for(j=0;j<N;j++)
                    printf("%d ",mat[i][j]);
                printf("\n");
            }

            getch();*/
        }

        printf("Case #%d: %d\n",_case++,res.size());
        sort(res.rbegin(),res.rend());
        for(i=0;i<res.size();i++)
            printf("%d %d\n",res[i],mp[res[i]]);

    }

    return 0;
}

void color(int ii,int jj,int val)
{
    int l1=ii+val,l2=jj+val,i,j;

    //printf("l1=%d,l2=%d\n",l1,l2);

    for(i=ii;i<l1;i++)
    {
        for(j=jj;j<l2;j++)
            mat[i][j]=-1;
    }
    //printf("l1=%d,ii=%d\n",l1,ii);

    return;


}

int Find_max(int ii,int jj,int v)
{
    if(ii+v>M||jj+v>N)
        return v-1;
    int ret=1,i,j,flag,f,g;

    if(mat[ii][jj]==0) flag=0;
    else flag=1;
    f=flag;

    for(i=ii;i<ii+v;i++)
    {
        flag=f;
        for(j=jj;j<jj+v;j++)
        {
            if(mat[i][j]==-1)
                return v-1;
            else if(flag)
            {
                if(mat[i][j]!=1)
                    return v-1;
            }
            else{
                if(mat[i][j]!=0)
                    return v-1;
            }

            if(flag) flag=0;
            else flag=1;
        }
        if(f) f=0;
        else f=1;
    }
    return Find_max(ii,jj,v+1);
}
