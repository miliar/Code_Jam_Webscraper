#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;


struct transform{
        char one,two;
        char result;
};
struct oppose{
        char one,two;
};


vector<transform> Trans;
vector<oppose> Oppos;
string answer;

void Insert( char in);
int max(int a, int b)
{return (a>b)?a:b;}
int min(int a, int b)
{return (a<b)?a:b;}
int get_diff(int a, int b)
{return max(a,b)-min(a,b);}

char getTransformation(char a, char b)
{
if (Trans.size()==0)
        return 0;
  for(int i=0;i<Trans.size();i++)
  {
    if ((Trans.at(i).one==a && Trans.at(i).two==b) ||
        (Trans.at(i).one==b && Trans.at(i).two==a) )
    {
      return Trans.at(i).result;
    }
  }

    return 0;
}

bool Transform(char in)
{
if(answer.size()==0)
{
        answer=in;
        return false;
}

  char result=getTransformation(answer.at(answer.size()-1),in);
  if(result !=0)
  {
        answer=answer.substr(0,answer.size()-1);
        Transform(result);
        return true;
  }
  answer+=in;
  return false;
}

bool inAnswer(char a)
{
  for(int i=0;i<answer.size();i++)
  {
    if(answer.at(i)==a)
      return true;
  }
  return false;
}

bool doesOppose(char in)
{
  for(int q=0; q<( Oppos.size());q++)
  {
        if(Oppos.size()==0){break;}
    if(Oppos.at(q).one==in)
      {
        if(inAnswer(Oppos.at(q).two))
        return true;
    }
    else if(Oppos.at(q).two==in)
    {
      if(inAnswer(Oppos.at(q).one))
        return true;
    }
  }

  return false;
}

void Insert( char in)
{
 if(! Transform(in))
 {//return;     //answer+=in;
 }

  if(answer.size()>0 && doesOppose(answer.at(answer.size()-1)))
  {
  answer="";
  }
  else
  {
  //answer+=in;
  }
}


int main()
{
        int numCases;
        int C,D,N;

        transform tmp_t;
        oppose tmp_o;
        string tmp_s;

        cin>>numCases>>ws;
        for(int k=1;k<=numCases;k++)
        {
                answer="";
                Trans.clear();
                Oppos.clear();
                cin>>C;
                for(int d=0;d<C;d++)
                {
                    cin>>tmp_s;
                    tmp_t.one=tmp_s.at(0);
                    tmp_t.two=tmp_s.at(1);
                    tmp_t.result=tmp_s.at(2);
                    Trans.push_back(tmp_t);

                }
                cin>>D;
                for(int i=0; i<D; i++)
                {
                  cin>>tmp_s;
                  tmp_o.one=tmp_s.at(0);
                  tmp_o.two=tmp_s.at(1);
                  Oppos.push_back(tmp_o);
                }

                cin>>N;
                cin>>tmp_s;
                int tmp_i;

                for(int i=0; i<tmp_s.size();i++)
                {
                  Insert(tmp_s.at(i));
                }

                cin>>ws;

                //solve

               cout<<"Case #"<<k<<": "
               /*ANSWER*/
               <<"[";
               for(int i=0;i<answer.size()-1;i++)
               {if(answer.size()==0)break;
               cout<<answer.at(i)<<", ";
               }
               if(answer.size()){cout<<answer.at(answer.size()-1);}
               cout
               <<"]"
               <<endl;
        }

return 0;
}
