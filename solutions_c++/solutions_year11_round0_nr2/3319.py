#include <set>
#include <map>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

int main()
{
    int N = 0;
    int temp = 0;
    int size = 0;
    char a, b, c;
    map<pair<char, char>, char> combine;
    set<pair<char, char> >  oppose;
    vector<char> output;
    
    pair<char, char> curr_pair;
    
    scanf("%d", &N);
    
    for (int i = 1; i <= N; i++)
    {
        combine.clear();
        oppose.clear();
        output.clear();
        
        //scan for element combinations
        scanf("%d", &temp);
        while (temp--)
        {
              scanf(" %c%c%c ", &a, &b, &c);
              combine[make_pair(a, b)] = c;
              combine[make_pair(b, a)] = c;
        }
        
        //scan for element oppositions
        scanf("%d", &temp);
        while (temp--)
        {
              scanf(" %c%c ", &a, &b);
              oppose.insert(make_pair(a, b));
              oppose.insert(make_pair(b, a));
        }
        
        //scan for the output
        scanf("%d", &temp);
        while (temp--)
        {
              scanf(" %c", &a);
              size = output.size();
              
              if (size > 0)
              {
                  curr_pair = make_pair(a, output[size-1]);
                  if (combine.find(curr_pair) != combine.end())
                  {
                     output[size-1] = combine[curr_pair];
                     a = output[size-1];
                  }
                  else
                      output.push_back(a);
              }
              
              else
                  output.push_back(a);
              
              for (unsigned int i = 0; i < output.size(); i++)
              {
                  if (oppose.find(make_pair(output[output.size() - 1], output[i])) != oppose.end())
                  {
                     output.clear();
                     break;
                  }
              }
        }
        
        printf("Case #%d: [", i);
        for (unsigned int i = 0; i < output.size(); i++)
        {
            printf("%c", output[i]);
            if (i != output.size() - 1)
               printf(", ");
        }
        printf("]\n");
    }
    
    return 0;
}
