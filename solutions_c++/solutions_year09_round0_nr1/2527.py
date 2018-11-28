#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>

using namespace std;


int L;
int ctr;
vector<vector<char> >s;
vector<string>dict;

int check(string str)
{
    for(int i=0;i<dict.size();i++)
        if(str==dict[i])
            return 1;

    return 0;
}


void func(string str, vector<string> mydict)
{
//cout<<"\n##"<<str.length()<<"##\n";
  //  cout<<mydict.size()<<"\n";;
    if(mydict.empty())
        return;

    int len=str.length();
    if(len==L)
    {
//        if(check(str))
  //          ctr++;
        ctr+=mydict.size();
        return;
    }

    for(int i=0;i<s[len].size();i++)
    {
        str.push_back(s[len][i]);

        vector<string>temp;
        //temp=delfromdict(mydict,temp,str[str.length()-1],str.length()-1);



        for(int k=0;k<mydict.size();k++)
        {
            if(mydict[k][str.length()-1]!=str[str.length()-1])
            {
    //            cout<<k;
                temp.push_back(mydict.begin()[k]);
                mydict.erase(mydict.begin()+k);
                k--;
            }

        }




        //str[len]=s[len][i];
        //str[len+1]='\0';
        //getchar();
    //cout<<str<<'\n';
        //getchar();

        if(!mydict.empty())
        {
            func(str,mydict);
        }

        for(int k=0;k<temp.size();k++)
            mydict.push_back(temp[k]);


        //str[len]='\0';
        str.erase(str.length()-1);


    }

}




int main()
{

int d,n,ca=1;
string temp;
char te[25];
cin>>L>>d>>n;

getchar();

for(int i=0;i<d;i++)
{
    //cin.getline(te,L);
    cin>>temp;
    //dict.push_back(te);
    dict.push_back(temp);
}

while(n-->0)
{
    ctr=0;
    s.clear();
    //cin.getline(te,'\n');
    cin>>temp;
    //cout<<temp<<'\n';
    for(int i=0;i<temp.length();i++)
    {
 //       cout<<'\n';
        //s.push_back(vector<char>);
        vector<char> t;

        if(temp[i]=='(')
        {
            i++;
            while(temp[i]!=')')
            {
                t.push_back(temp[i]);
                i++;

   //             cout<<temp<<' ';

            }
        }

        else
            t.push_back(temp[i]);

        s.push_back(t);

    }

//cout<<"\n.."<<s.size()<<"..\n";
/*
    for(int i=0;i<s.size();i++)
    {
        for(int j=0;j<s[i].size();j++)
        {
            cout<<s[i][j]<<' ';

        }

        cout<<'\n';
    }
*/
    string x="";

//cout<<"\n\n\n.............."<<dict.size()<<"...............\n\n\n";

    func(x,dict);

    cout<<"Case #"<<ca++<<": "<<ctr<<'\n';



}





getchar();
getchar();
getchar();
getchar();
getchar();

}





