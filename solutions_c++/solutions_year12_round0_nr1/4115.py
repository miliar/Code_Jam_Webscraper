//
//  main.cpp
//  Code_Jam
//
//  Created by 용 최 on 12. 4. 13..
//  Copyright (c) 2012년 soaryong.c@gmail.com. All rights reserved.
//

#include <stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, const char * argv[])
{
//    int n;
//    string str;
//    char alpha[26];
//    cin>>n;
//    for(int i =0 ;i<n;i ++)
//    {
//        cin>>str;
//        for(int j =0 ;j<str.length();j++){
//            if(str[j] == ' ')
//                continue;
//            else
//                
//        }
//    }
    
//    3
//    ejp mysljylc kd kxveddknmc re jsicpdrysi
//    our language is impossible to understand
//    rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
//    there are twenty six factorial possibilities
//    de kr kd eoya kw aej tysr re ujdr lkgc jv
//    so it is okay if you want to just give up
//    
//    FILE *in = fopen("/Users/soaryong/dev/Code_Jam/Code_Jam/sample.in","rt");
//    int n,i,j;
//    char a[26]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},str1[200],str2[200],b;
//    fscanf(in,"%d",&n);
//    fscanf(in,"%c",&b);
//
//    for(i=0;i<n;i++)
//    {
//        fflush(stdin);
//        fgets(str1, 200, in);
//        printf("%s",str1);
//        fflush(stdin);
//        fgets(str2, 200, in);
//        printf("%s",str2);
//        for(j=0;j<strlen(str1)-1;j++){
//            if(str1[j]==' ')
//                continue;
////            printf("%d%c ",str1[j]-'a',str2[j]);
//            a[str2[j]-'a']=str1[j];
//        }
//    }
//    for(i=0;i<26;i++)
//    {
//        printf("'%c', ",a[i]);
//    }
//    
    char alpha[26]={'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};
    char a[26];
    FILE *in = fopen("/Users/soaryong/dev/Code_Jam/Code_Jam/sample.in","rt");
    FILE *out = fopen("/Users/soaryong/dev/Code_Jam/Code_Jam/sample.out","wt");
    int n,i,j;
    char str1[200],b;
    fscanf(in,"%d",&n);
    fscanf(in,"%c",&b);
    
    for(i=0;i<26;i++){
        a[alpha[i]-'a']='a'+i;
    }
    for(i=0;i<n;i++)
    {
        fprintf(out,"Case #%d: ", i+1);
        fflush(stdin);
        fgets(str1, 200, in);
        for(j=0;j<strlen(str1)-1;j++){
            if(str1[j]==' ')
                fprintf(out,"%c",str1[j]);
            else 
                fprintf(out,"%c",a[str1[j]-'a']);
        }
        fprintf(out,"\n");
    }
    return 0;
}


