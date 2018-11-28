#include <stdio.h>




int main()
{
    int i,j,l,d,n,k,f,z,p;
    char words[5001][20];
    char s[1000];
    char m[5001];
    char a[130];
    
    scanf("%hhd %d %d",&l,&d,&n);
    
    for (i=0;i<d;++i)
        scanf("%s",words[i]);
    
   // printf("%d\n",d);
    
    for (k=0;k<n;++k)
    {
        scanf("%s",s);
        for (i=0;i<d;++i)
            m[i]=1;
            
        for (p=0;s[p];++p);
        
        z=0;
        f=0;
        
        while (f<p)
        {
              if (s[f]=='(')
              {
                 
                 for (i='a';i<'z';++i)
                     a[i]=0;
                 for (f++;s[f]!=')';++f)
                     a[s[f]]=1;
                     
                 for (i=0;i<d;++i)
                     if (a[words[i][z]]==0)
                        m[i]=0;
              }
              else    
               for (i=0;i<d;++i)
                     if (words[i][z]!=s[f])
                        m[i]=0; 
              ++f;
              ++z;                
        }
        j=0;
        for (i=0;i<d;++i)
            if (m[i])
               ++j;
        printf("Case #%d: %d\n",k+1,j);
    }
    
    return 0;
}
