#include <iostream>
using namespace std;
main()
{
  int t; cin >> t;
  for(int count=1;count<=t;count++) 
  {
    int n,k; cin >> n >> k;
    printf("Case #%d: ",count);
    puts((k+1)&((1<<n)-1)?"OFF":"ON");
  }
}
