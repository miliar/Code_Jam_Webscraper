#include <iostream>
#include <fstream>
using namespace std;

int get2dig(int a, int b)
{
    int result = 0;
    for (int i = a; i <= b; i++)
    {
      int i_1 = (i%10)*10+(i/10);
      if (i_1<i & i_1>=a)
        result++;
    }
    return result;
}
int get3dig(int a, int b)
{
    int result = 0;
    for (int i = a; i <= b; i++)
    {
        int i_1 = (i%100)*10+(i/100);
        int i_2 = (i_1%100)*10+(i_1/100);
        if (i_1<i && i_1>=a) result++;
        if (i_2<i && i_2>=a && i_2 != i_1 ) result++;

    }
    return result;
}
/*
int get4dig(int a, int b)
{
    int result = 0;
    for (int i = a; i <= b; i++)
    {
      int i_1 = (i%1000)*10+(i/1000);
      int i_2 = (i_1%1000)*10+(i_1/1000);
      int i_3 = (i_2%1000)*10+(i_2/1000);
      if (i_1<i && i_1>a) result++;
      if (i_2<i && i_2>a && i_2 != i && i_2 != i_1) result++;
      if (i_3<i && i_3>a && i_3 != i && i_3 != i_2 && i_3 != i_1) result++;
    }
    return result;
}
*/
int main(){

  ifstream fin;
  fin.open("C-small-attempt1.in");
  ofstream fout;
  fout.open("C-small-submit.out");

  int nCase;
  fin >> nCase;

  for (int i = 1; i <= nCase; i++){
    int a,b,n;
    fin >> a >> b;
    if (b<10)
    {
        n = 0;
    } else if (b<100)
    {
        n = get2dig((a>=10?a:10),b);
    } else if (b<=1000)
    {
        if (b==1000) b = 999;
        if (a<100)
        {
            n = get2dig((a>=10?a:10),99) + get3dig(100,b);
        }
        else
        {
            n = get3dig(a,b);
        }
    }
    //else n = get4dig(a,b);

    fout << "Case #" << i << ": " << n << endl;
    cout << "Case #" << i << ": " << n << endl;
  }

  fin.close();
  fout.close();
  return 0;
}
