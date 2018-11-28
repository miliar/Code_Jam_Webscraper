#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
main()
{
        int let,word,inp;
        scanf("%d %d %d",&let,&word,&inp);
        char dict[word][let+2];
        char c;
        //cin>>c;
        int num=0;
        int flag[word];
        int cnt,br=0;
        for(int i=0;i<word;i++)
                scanf("%s",&dict[i]);
        scanf("%c",&c);
        int cas=0;
        while(inp--)
        {
                br=0;
                cnt=0;
                for(int i=0;i<word;i++)
                        flag[i]=-1;
                //cin>>c;
                //if(
                num=-1;
                while(1)
                {
                        scanf("%c",&c);
                        if(c=='\n')
                                break;
                        if(c=='(')
                        {
                                br=1;
                                num++;
                        }
                        else if(br==0&&c!='(')
                                num++;
                        else if(br==1&&c==')')
                        {

                                br=0;
                                continue;
                        }


                for(int i=0;i<word;i++)
                {
                        if(flag[i]==-2)
                                continue;
                        if(dict[i][num]==c)
                        {
                                if(flag[i]==num-1)
                                {

                                        flag[i]=num;
                                        if(num==let-1)
                                                cnt++;
                                }
                                else flag[i]=-2;

                        }
                        if(flag[i]<num-1)
                                flag[i]=-2;
                }


        }
                cout<<"Case #"<<++cas<<": "<<cnt<<endl;
        }
}
