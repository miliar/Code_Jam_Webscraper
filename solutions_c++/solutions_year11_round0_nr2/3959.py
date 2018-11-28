#include<iostream>
#include<string>
using namespace std;
char comb(char,char);
bool oppo(char);
int C,D,count;
string combine[37],oppose[29],output;
int main()
{
    bool flag;
    int T,N;
    int i,tcase=1;
    string input;
    char temp;
    cin>>T;
    while(T--)
    {
        cin>>C;
        output="";
        count=1;
        for(i=0;i<C;i++)
        cin>>combine[i];
        cin>>D;
        for(i=0;i<D;i++)
        cin>>oppose[i];
        cin>>N;
        cin>>input;
        output=output+input[0];
        for(i=1;i<N;i++)
        {
            //cout<<output;
            if(count>=1)
            {
              temp=comb(output[count-1],input[i]);
              //cout<<"t"<<temp;
              if(temp!='*')
              {
                  output=output.substr(0,count-1);
              //output[count-1]=temp;
              output+=temp;
              }
              else
              {
                flag=oppo(input[i]);
                if(flag)
                {
      //              cout<<"helooooooooooooooo";
                    output="";
                    count=0;
                }
                else
                {
                    output+=input[i];
                    count++;
                }
              }
            }
            else
            {
            output+=input[i];
            count++;
            }
        }
    if(output.length())
    {
        cout<<"Case #"<<tcase<<": [";
        for(i=0;i<output.length()-1;i++)
        cout<<output[i]<<", ";
        cout<<output[i]<<"]"<<endl;
    }
    else
    cout<<"Case #"<<tcase<<": []"<<endl;
    tcase++;
    }
}
char comb(char a,char b)
{
    int i;
    //cout<<a<<"\t"<<b<<endl;
 for(i=0;i<C;i++)
 {
  if((combine[i][0]==a && combine[i][1]==b) || (combine[i][1]==a && combine[i][0]==b) )
  return combine[i][2];
 }
 return '*';
}
bool oppo(char a)
{
    int i,j;
    char b;
    //cout<<a<<"\t"<<"b"<<endl;
    //cout<<"LEngth="<<output;
    for(j=0;j<output.length();j++)
    {
        b=output[j];
        for(i=0;i<D;i++)
        {
            if((oppose[i][0]==a && oppose[i][1]==b) || (oppose[i][1]==a && oppose[i][0]==b) )
            return true;
        }
    }
    return false;
}
