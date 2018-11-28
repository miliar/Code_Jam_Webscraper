#include<iostream>
#include<vector>
using namespace std;
int C,D,N,T;
char Com[3];
char Opp[2];


vector<char>data;
string temp;
char opp_temp;
bool m_o;
bool q;
int main()
{
cin>>T;
for(int j=0;j<T;j++)
{


    cin>>C;
    if(C)
    {
    cin>>temp;
    for(int i=0;i<3;i++)
     Com[i]=temp[i];
    }

    cin>>D;;
    if(D)
    {
        cin>>temp;
        for(int i=0;i<2;i++)
        Opp[i]=temp[i];
    }


    cin>>N>>temp;

    m_o=false;

      for(int i=0;i<temp.size();i++)
        {
          data.push_back(temp[i]);
          int bi=data.size();
          if(C && i>0 && bi>1)
          {

                if((data.at( bi-2)==Com[0] && data.at( bi-1)==Com[1])  || (data.at( bi-2)==Com[1] && data.at( bi-1)==Com[0]) )
                {
                        data.pop_back();
                        data.pop_back();
                        data.push_back(Com[2]);
                        continue;
                }

          }//EndofIf(C)
          if(D)
          {
            if(temp[i]==Opp[0])
            {
              for(int i=0;i<data.size();i++)
               {
                  if(data.at(i)==Opp[1])
                    {
                        data.clear();
                        break;
                    }
               }
            }

            else if(temp[i]==Opp[1])
            {
              for(int i=0;i<data.size();i++)
               {
                  if(data.at(i)==Opp[0])
                    {
                        data.clear();
                        break;
                    }
               }
            }
          }//end of if(D)
        }
    cout<<"Case #"<<j+1<<": [";
    for(int i=0;i<data.size();i++)
        {
            if(i)
            cout<<", ";
            cout<<data.at(i);
        }
    cout<<"]"<<endl;
    data.clear();
}
    return 0;
}
