#include <iostream>
#include <list>
#include <string>

using namespace std;
int T;//turnaround time is global to avoid passing it into the function

bool compare_times (string first, string second)
{
  for(int i=0;i<first.length();i++)
  {//first.length() = last.length() as the numbers are zero padded
   //so there is no need to check last.length()
    if(first[i]<second[i]) return true;
    else if(first[i]>second[i]) return false;
  }

  //times are identical if this point is reached
  return true;
}

string add_turnaround (string current)
{
  int min = static_cast<int>(current[3]-'0')*10 + static_cast<int>(current[4]-'0') + T;
  if(min<60)
  {
     current[3] = static_cast<char>(min/10+'0');
     current[4] = static_cast<char>(min%10+'0');
    return current;
  }

  //only reach here if the hour must also be incrimented
  min-=60;
  int hour = static_cast<int>(current[0]-'0')*10 + static_cast<int>(current[1]-'0') + 1;
    current[0] = static_cast<char>(hour/10+'0');
    current[1] = static_cast<char>(hour%10+'0');
    current[3] = static_cast<char>(min/10+'0');
    current[4] = static_cast<char>(min%10+'0');
  return current;     
}

int main (int argc, char ** argv)
{
    int N,NA,NB;
    list<string> NA_out, NB_in, NB_out, NA_in;
    string bufr;

    cin >> N;
    for(int i=0;i<N;i++)
    {
      if(i!=0)
      {
        NA_out.clear();
        NB_in.clear();
        NB_out.clear();
        NA_in.clear();
        cout << endl;
      }
      
      cin >> T >> NA >> NB;
      getline(cin,bufr); // eat the newline character
      
      for(int j=0;j<NA;j++)
      {
        cin >> bufr;
        NA_out.push_front(bufr);
        cin >> bufr;
        NB_in.push_front(add_turnaround(bufr));
      }
      for(int j=0;j<NB;j++)
      {
        cin >> bufr;
        NB_out.push_front(bufr);
        cin >> bufr;
        NA_in.push_front(add_turnaround(bufr));
      }
      
      NA_out.sort(compare_times);
      NB_in.sort(compare_times);
      NB_out.sort(compare_times);
      NA_in.sort(compare_times);

      if(!NA_in.empty() && !NA_out.empty())
      {//if there are trains dealing with station A
        for(;!NA_in.empty()&&!NA_out.empty();NA_in.pop_front())
        {
          for(;!NA_out.empty();NA_out.pop_front())
          {
            if(compare_times(NA_in.front(),NA_out.front()))
            {
              NA--;
              NA_out.pop_front();
              break;
            }
          }        
        }
      }
      
      if(!NB_in.empty() && !NB_out.empty())
      {//if there are trains drealing with station B
        for(;!NB_in.empty()&&!NB_out.empty();NB_in.pop_front())
        {
          for(;!NB_out.empty();NB_out.pop_front())
          {
            if(compare_times(NB_in.front(),NB_out.front()))
            {
              NB--;
              NB_out.pop_front();
              break;
            }
          }
        }
      }      
           
      cout << "Case #" << (i+1) << ": " << NA << " " << NB;
    }

    return 0;
}
