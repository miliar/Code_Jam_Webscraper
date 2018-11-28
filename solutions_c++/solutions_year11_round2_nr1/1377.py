#include<cstdio>
#include<algorithm>
using namespace std;

int map[105][105];
double win[105],sum[105],w[105],ow[105],oow[105];
int main()
{
    int cas,n,m,i,j,k;
    char c;
    double tmp,t2;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&cas);
    for(k = 1;k <= cas;k++)
    {
        scanf("%d",&n);
	scanf("%c",&c);
	for(i = 0;i < n;i++)
	{
	  tmp = 0;
	  t2 = 0;
	  for(j = 0;j < n;j++)
	  {
	      do{
               scanf("%c",&c);
              }while(c == ' ' || c == '\n');
	      
	      if(c == '.')
		map[i][j] = 0;
	      else if(c == '0')
	      {
		map[i][j] = -1;
	        tmp++;
	      }
	      else if(c == '1')
	      {
		map[i][j] = 1;
		tmp++;
		t2++;
	      }
	  }
	  win[i] = t2;
	  sum[i] = tmp;
	  if(tmp != 0)
	    w[i] = t2 / tmp;
	  else
	    w[i] = 0;
	}
	
	for(i = 0;i < n;i++)
	{
	  tmp = 0;
	  t2 = 0;
	  for(j = 0;j < n;j++)
	  {
	    if(map[i][j] != 0)
	    {
	      tmp++;
	      if(sum[j] == 0 || sum[j] == 1 || win[j] == 0)
		t2 = t2;
	      else
	      {
	      if(map[j][i] == 1)
		t2 = t2 +  (win[j] - 1) * 1.0 / (sum[j] - 1);
	      else
		t2 = t2 +  win[j] * 1.0 / (sum[j] - 1);	
	      }
	    }
	  }
	  if(tmp != 0)
	    ow[i] = t2 / tmp;
	  else
	    ow[i] = 0;
	}
	
	for(i = 0;i < n;i++)
	{
	  tmp = 0;
	  t2 = 0;
	  for(j = 0;j < n;j++)
	  {
	    if(map[i][j])
	    {
	      tmp++;
	      t2 += ow[j];
	    }
	  }
	  if(tmp != 0)
	    oow[i] = t2 / tmp;
	  else
	    oow[i] = 0;
	}

        printf("Case #%d:\n",k);
	for(i = 0;i < n;i++)
	{
	  tmp = 0.25 * w[i] + 0.50 * ow[i] + 0.25 * oow[i];
	  printf("%.7lf\n",tmp);
	}
    }

    return 0;
}
