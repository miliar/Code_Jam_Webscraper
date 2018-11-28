//
//  main.cpp
//  Google Codejam Qualification Round
//
//  Created by Seung Ho Jang on 12. 4. 15..
//  Copyright (c) 2012년 shjang1992@hotmail.com. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main(int argc, const char * argv[])
{
    FILE *fp = fopen("/Users/FrozenGuy/XCode Projects/Google Codejam Qualification Round/Google Codejam Qualification Round/A-small-attempt6.in","r");
    char input[200];
    
    FILE * output = fopen("/Users/FrozenGuy/XCode Projects/Google Codejam Qualification Round/Google Codejam Qualification Round/output.txt","w");
    
    string replacements = "";
    replacements.resize(26);
    string ex[3];
    string ans[3];
    
    ex[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    ex[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    ex[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    
    ans[0] = "our language is impossible to understand";
    ans[1] = "there are twenty six factorial possibilities";
    ans[2] = "so it is okay if you want to just give up";
    
    for(int index = 0;index < 3;++index)
        for(int i=0;i<ex[index].length();++i)
            if(ex[index][i] != ' ')
                replacements[ex[index][i] - 'a'] = ans[index][i];
    
    replacements[25] = 'q';//z
    replacements[16] = 'z';//q
    
    int lines = 0;
    fscanf(fp,"%d",&lines);
    
    cout<<lines<<endl;
    fgets(input,100,fp);
    
    for(int cur_line = 1;cur_line<=lines;++cur_line)
    {
        //fscanf(fp,"%s",&input);
        fgets(input, 102, fp);
        
        for(int i=0;input[i] != '\n' && input[i] != 0;++i)
        {
            if(input[i] != ' ')
                input[i] = replacements[input[i] - 'a'];
        }
            
        cout<<"Case #"<<cur_line<<": "<<input;
        fprintf(output,"Case #%d: %s",cur_line,input);

    }
    
    
    return 0;
}