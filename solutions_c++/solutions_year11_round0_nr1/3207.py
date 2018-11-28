# include <iostream>
# include <cmath>

using namespace std;

int main ()
{
    int test;
    cin>>test;
    for (int testid = 1;testid <=test;testid++)
    {
        int ans = 0;
        int num;
        int Opos = 1;
        int Bpos = 1;
        int Obuf = 0;
        int Bbuf = 0;
        int diff;
        int temp;
        cin>>num;
        char ch;
        for (int i = 0;i < num;i++)
        {
            cin>>ch;
            cin>>temp;
            if (ch == 'O')
            {
                  diff = std::abs(temp - Opos);
                  if (Obuf >= diff)
                  {
                     ans += 1;
                     Bbuf += 1;
                  }
                  else
                  {   
                      ans += (diff - Obuf + 1);
                      Bbuf += (diff - Obuf + 1);
                  }
                  Obuf = 0;
                  Opos = temp;
            }
            else
            {
                  diff = std::abs(temp - Bpos);
                  if (Bbuf >= diff)
                  {
                     ans += 1;
                     Obuf += 1;
                  }
                  else
                  {   
                      ans += (diff - Bbuf + 1);
                      Obuf += (diff - Bbuf + 1);
                  }
                  Bbuf = 0;
                  Bpos = temp;
            }
        }                                  
        cout<<"Case #"<<testid<<": "<<ans<<endl;
    }    
    return 0;
}    
