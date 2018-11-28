#include <iostream>
#include <vector>
#include <string>

using namespace std;



int main()
{
    int  l=0,d=0,n=0,loop_i=0,i = 0,j = 0;
    cin>>l>>d>>n;
    vector <string> dict;
    string temp;
    
    // Creating the dictionary
    for(loop_i = 0;loop_i < d;loop_i++)
    {
        cin>>temp;
        dict.push_back(temp);
    }
    for(loop_i = 0;loop_i < n;loop_i++)
    {
        cin>>temp;
        vector <string> chk_lst;
        
        
        // Creating chk_lst from the string
        for(i=0;i<temp.size();i++)
        {
            if(temp[i]!='('&&temp[i]!=')')
            {
                chk_lst.push_back(temp.substr(i,1));
                
            }
            if(temp[i] == '(')
            {
                int j=0;
                while(temp[i+j]!=')')
                {
                    j++;
                }
                chk_lst.push_back(temp.substr(i+1,j-1));
                i = i+j;
            }
        }
        
        
        int check_value = 0;
        int count = 0;
        for(i=0;i<d;i++)
        {
            int chk_val =0;
            for(int j =0;j<l;j++)
            {
                
                for(int k =0;k<chk_lst[j].size();k++)
                {
                    if(dict[i][j]==chk_lst[j][k])
                    {
                        chk_val = chk_val | (1<<j);
                    }
                }
                check_value = check_value | (1<<j);
            }
            if(check_value == chk_val)
            {
                count ++;
                check_value = 0;
            }
            
        }
        cout<<"Case #"<<loop_i+1<<": "<<count<<endl;
            
            
    }
    
}
