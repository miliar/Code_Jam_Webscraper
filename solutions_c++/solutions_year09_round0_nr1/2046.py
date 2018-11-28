#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

void checkValid(string to_match, vector<string> still_valid, int level, int index,int& counter)
{ 
    if (index >= to_match.length())
    {
       counter = still_valid.size();
       return;          
    }
    
    vector<bool> is_valid(still_valid.size(),0);
    vector<string> new_valid;
   if (to_match[index] == '(')
    {
         int temp_level = index;
         vector<char> letters;
         temp_level++;
         while(to_match[temp_level]!=')')
         {
          letters.push_back(to_match[temp_level]);
          temp_level++;                         
         }
         temp_level++;

         
         for (int i = 0; i < letters.size();i++)
         {
             for (int j = 0; j < still_valid.size(); j++)
             {
                 if (letters[i]==still_valid[j][level])
                 {
                    is_valid[j] = 1;                                      
                 }
             }         
         }
         
         for (int i = 0; i < is_valid.size(); i++)
         {
             if (is_valid[i])
             {
                new_valid.push_back(still_valid[i]);                
             }
         }
         index = temp_level;
         checkValid(to_match,new_valid,level+1,index,counter);
    }
    else
    {
         for (int j = 0; j < still_valid.size(); j++)
         {
             if (to_match[index]==still_valid[j][level])
             {
                is_valid[j] = 1;                                               
             }
         } 
         for (int i = 0; i < is_valid.size(); i++)
         {
             if (is_valid[i])
             {
                new_valid.push_back(still_valid[i]);                
             }
         }
         checkValid(to_match,new_valid,level+1,index+1,counter);
    }

    
}

int main()
{
    ifstream freader("A-small.in");
    ofstream fwriter("A-small.out");
    
    int L, D, N;
    vector<string> dict_words;
    vector<string> test_cases;
    string temp;
    
    freader >> L >> D >> N;
    getline(freader,temp);
    for (int i = 0; i < D; i++)
    {
        getline(freader,temp);
        dict_words.insert(dict_words.end(),temp);
    }
    for (int i = 0;  i < N; i++)
    {
        getline(freader,temp);
        test_cases.insert(test_cases.end(),temp);        
    }
    
    //for (int i = 0 ; i < dict_words.size(); i++) cout << dict_words[i] << endl;
    ///cout << endl;
    for (int i = 0 ; i < test_cases.size(); i++)
    {
        int counter = 0;
        checkValid(test_cases[i],dict_words,0,0,counter);    
        fwriter << "Case #" << i+1 << ": " << counter << endl;
    }

    fwriter.close();
    freader.close();
    return 0;
    //getch();
}
