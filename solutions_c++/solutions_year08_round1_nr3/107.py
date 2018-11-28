#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
const string a[] = {"005", "027", "143", "751", "935", "607", "903", "991", "335", "047",
                    "943", "471", "055", "447", "463", "991", "095", "607", "263", "151", 
                    "855", "527", "743", "351", "135", "407", "903" ,"791" ,"135" ,"647"};

int n, casen;

void init()
{
     scanf("%d", &n);
}

void work()
{
     cout << a[n - 1] << endl;
}

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.ans", "w", stdout);
    scanf("%d", &casen);
    for (int i(1); i <= casen; ++i)
    {
        init();
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
