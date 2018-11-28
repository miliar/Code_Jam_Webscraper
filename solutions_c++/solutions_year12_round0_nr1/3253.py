#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    char trans[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int count,len;
    int i,j;
    char s[104];
    FILE *fp,*f;
    
    fp = fopen("D:\\A-small-attempt5.in","r");
    f = fopen("D:\\ans.txt","w");
    if(fp == NULL)printf("false");
    
    fscanf(fp,"%d",&count);
    fgets(s,200,fp);
    for(i=0;i<count;i++){
        fgets(s,200,fp);
        len = strlen(s);
        for(j=0;j<len;j++){
            if(s[j]<='z'&&s[j]>='a')s[j] = trans[s[j]-'a'];
        }
        fprintf(f,"Case #%d: %s",i+1,s);
    }
    
    fclose(fp);
    fclose(f);
    system("pause");
    return 0;
}
