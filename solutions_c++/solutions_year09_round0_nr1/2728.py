#include<iostream>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
  int L,D,N,i,cnt,sz,j,k,p,t;
  bool flag;
  scanf("%d %d %d",&L,&D,&N);getchar();
  char str[D+5][L+4],arr[50000],dicsize[D],ch;
  for(i=0;i<D;i++)
	{
        gets(str[i]);
		dicsize[i]=strlen(str[i]);
	}
   for(i=0;i<N;i++)
	{
        gets(arr);
	    cnt=0;
        sz=strlen(arr);
		for(j=0;j<D;j++)
		{
			p=dicsize[j];
            for(k=0,t=0;t<sz && k<p;k++,t++)
				{
				    flag=false;
					ch=str[j][k];
                   if(arr[t]=='(')
					{
                      while(arr[t]!=')')
						{
                          t++;
						  if(!flag && arr[t]==ch)flag=true;
						}
					}
					else if(arr[t]==ch)flag=true;
					if(!flag)break;
				}
               if(flag) cnt++;
		}
		printf("Case #%d: %d\n",i+1,cnt);
	}
   
  return 0;
}
