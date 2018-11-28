#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;
int a,b,c,d,e,f,g,h,i,j,k;
int zz[27][27];
vector<int> v[27],hsl;
int bole[27];
int main()
{
    //freopen("magic.in","r",stdin);
    //freopen("magic.out","w",stdout);
    scanf("%d",&a);
    for (b=1;b<=a;b++)
    {
        memset(zz,0,sizeof(zz));
        scanf("%d",&c);
        char ch;
        char s[4];
      //  printf("tes\n");
        for (d=1;d<=c;d++)
        {
            scanf("%c",&ch);
            scanf("%s",s);
            zz[(int)s[0]-65][(int)s[1]-65]=(int)s[2]-65;
            zz[(int)s[1]-65][(int)s[0]-65]=(int)s[2]-65;
        }
        //printf("tes %s\n",s);
        for (d=0;d<=26;d++)
        v[d].clear();
        scanf("%d",&e);
        for (d=1;d<=e;d++)
        {
          //  printf("%d\n",e);
            scanf("%c",&ch);
            scanf("%s",s);
            v[(int)s[0]-65].push_back((int)s[1]-65);
            v[(int)s[1]-65].push_back((int)s[0]-65);
        }
        //printf("%d\n",v[22][0]);
        //printf("tes\n");
        scanf("%d",&f);
        scanf("%c",&ch);
        char s2[200];
        scanf("%s",&s2);
        f=strlen(s2);
        memset(bole,0,sizeof(bole));
        hsl.clear();
        hsl.push_back((int)s2[0]-65);
        bole[(int)s2[0]-65]++;
        for (d=1;d<f;d++)
        {
			//printf("%d\n",bole[22]);
            if (hsl.size()==0)
            {
               hsl.push_back((int)s2[d]-65);
               bole[(int)s2[d]-65]+=1;
			}
            else
            {
            if (zz[(int)s2[d]-65][hsl[hsl.size()-1]]!=0)
            {
               i=hsl[hsl.size()-1];
               bole[i]-=1;
               hsl.pop_back();
               hsl.push_back(zz[(int)s2[d]-65][i]);    
            }
            else
            {
                for (g=0;g<v[(int)s2[d]-65].size();g++)
                {
                    if (bole[v[(int)s2[d]-65][g]]!=0)
                    {
					  // printf("%d %d\n",s2[d]-65,d);
                       hsl.clear();
                       memset(bole,0,sizeof(bole));                  
                    }
                }  
                if (hsl.size()!=0){
					hsl.push_back((int)s2[d]-65);
					bole[(int)s2[d]-65]+=1;
				}
            }
            }
        }
        printf("Case #%d: [",b);
        for (g=0;g<(int)hsl.size()-1;g++)
           printf("%c, ",hsl[g]+65);
        if ((int)hsl.size()>0)
        printf("%c",hsl[(int)hsl.size()-1]+65);
        printf("]\n");
    }
    scanf("%d",&a);
}
