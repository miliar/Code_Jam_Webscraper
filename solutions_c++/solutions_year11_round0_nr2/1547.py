#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<utility>

using namespace std;

bool find(vector<char> list, char ch)
{
    for (int i=0; i<list.size(); i++)
        if (list[i]==ch)
            return true;
    return false;
}

int main()
{
    int t, count, c, d, n;
    cin >> t;
    count=0;
    vector<char> list;
    vector<string> clist, dlist;
    while (count<t)
    {
        count++;
        int i;
        string temp;
        list.clear();
        clist.clear();
        dlist.clear();
        cin >> c;
        for (i=0; i<c; i++)
        {            
            cin >> temp;
            clist.push_back(temp);       
        }        
        cin >> d;
        for (i=0; i<d; i++)
        {            
            cin >> temp;
            dlist.push_back(temp);            
        }        


        cin >> n;
        char ch;
        for (i=0; i<n; i++)
        {            
            cin >> ch;
            int j;
            for (j=0; j<c; j++)
            {
                if (ch==clist[j][0] && list.back()==clist[j][1])
                {
                    list.pop_back();
                    list.push_back(clist[j][2]);
                    break;
                }
                else 
                    if (ch==clist[j][1] && list.back()==clist[j][0])
                    {
                        list.pop_back();
                        list.push_back(clist[j][2]);
                        break;
                    }
            }                        

            if (j==c)           
            {
                for (j=0; j<d; j++)
                {
                    if (dlist[j][0]==ch)
                    {       
                        if (find(list, dlist[j][1]))
                        {
                            list.clear();
                            break;
                        }
                    }
                    else if (dlist[j][1]==ch)
                    {       
                        if (find(list, dlist[j][0]))
                        {
                            list.clear();
                            break;
                        }
                    }
    
                } 
               if (j==d)
                    list.push_back(ch);

            }
 
        }    

        cout << "Case #" << count << ": [";
        int k=list.size()-1;
        for (int i=0; i<k; i++)
            cout << list[i] << ", ";

        if (!list.empty())
            cout << list.back();
        cout << "]" <<endl;
    }
    
}
