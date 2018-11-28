#include<cstdio>
#include<cstring>


int main()
{
    char map[30],str[1100],train[1000],train2[1000];
    long len,i,j,k,l,T;
    strcpy(train,"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz");
    strcpy(train2,"our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq");
    len=strlen(train);
    
    for(i=0;i<len;i++)
    {
        map[train[i]-'a']=train2[i];                  
    }    
    //map[25]='q';
    //map[26]='\0';
    
    //freopen("A-small-attempt6.in","r",stdin);
	//freopen("A-small-attempt6.out","w",stdout);
	
    scanf("%ld",&T);
    getchar();
    j=0;
    while(T--)
    {
        gets(str);
        len=strlen(str);                
        if(len==0){T++;continue;}
        printf("Case #%ld: ",++j);;
        for(i=0;i<len;i++) 
        {
            if(str[i]>='a' && str[i]<='z')
            printf("%c",map[str[i]-'a']);                   
            else printf("%c",str[i]);
        }
        printf("\n");
    }
              
    return 0;    
}
