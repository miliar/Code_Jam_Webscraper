# include <iostream>
# include <vector>
# include <set>

using namespace std;

vector <string> split (string dir)
{
    vector <string> ret;  
    string temp = ""; 
    for (int i=0;i<dir.size ();i++)
    {               
       if (dir[i]!='/')
       {
           temp.push_back (dir[i]);
       }
       else
       {
           if (temp!="")
           {
              ret.push_back (temp);
              temp="";
           }   
       }
    }
    if (temp!="")
    {
       ret.push_back (temp);
       temp="";
    }             
    return (ret);
} 

int main ()
{
    int test;
    cin>>test;
    int index = 1;
    while (index <= test)
    {
          int N,M;
          cin>>N>>M;
          string temp;
          vector <string> temp11;
          set <string> commands;
          for (int i=0;i<N;i++)
          {
              cin>>temp;
              temp11 = split (temp);
              string temp2 = "";
              for (int j=0;j<temp11.size ();j++)
              {
                  temp2 += ("/" + temp11[j]);
                  if (commands.find (temp2) == commands.end ())
                  {
                       commands.insert (temp2);
                  }
              }                 
          }
          int count = 0;
          for (int i=0;i<M;i++)
          {
              cin>>temp;
              temp11 = split(temp);
              string temp2 = "";
              for (int j=0;j<temp11.size ();j++)
              {
                  temp2 += ("/" + temp11[j]);
                  if (commands.find (temp2) == commands.end ())
                  {
                       count++;             
                       commands.insert (temp2);
                  }
              }                             
          }
          cout<<"Case #"<<index<<": "<<count<<endl;
          index++;
    }     
    return 0;
}          
              
