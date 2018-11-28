#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>

using namespace std;

int main()
{
  int moze[15][30];
  int l,d,n;
  vector<string> rijeci;
  scanf("%d %d %d",&l,&d,&n);
  
  for(int i=0;i<d;i++)
  {
    string rijec;
    char rijecCh[20];
    scanf("%s", rijecCh); 
    rijec=rijecCh;
    rijeci.push_back(rijec);    
  }
  
  for(int i=0;i<n;i++)
  {
    char primjer[1000];
    int br=0;
    scanf("%s",primjer);
    memset(moze,0,sizeof(moze));
    for(int j=0;j<l;j++)
    {
      if(primjer[br]=='(')
      {
        br++;
        while(primjer[br]!=')')
        {
          moze[j][primjer[br]-'a']=1;
          br++;
        }
        br++;
      }
      else
      {
        moze[j][primjer[br]-'a']=1;
        br++;
      }
    }
    
    int rez=0;
    for(int j=0;j<rijeci.size();j++)
    {
      int plus=1;
      for(int k=0;k<l;k++)
        if(moze[k][ rijeci[j][k] - 'a'] != 1 ) { plus=0; break; }
      rez+=plus;
    }
    printf("Case #%d: %d\n", i+1, rez);
  }
}
