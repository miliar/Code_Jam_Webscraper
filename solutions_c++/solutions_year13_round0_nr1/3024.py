#include<iostream>
#include<fstream>
#include<map>

using namespace std;

int computeResult(int arr[][4])
{
   int h_arr[4]={1, 1, 1, 1};
   int h_curr[4];
   int v_curr[4];
   int v_arr[4] = {1, 1, 1, 1};
   int dot_count = 0;
   int won = -1;
   bool break_flag = 0;
   bool dec_flag = 0;
   int f_d = 1, b_d = 1;

   for (int i=0; i<4; i++)
   {
    h_curr[i] = arr[i][0];
    v_curr[i] = arr[0][i];
    if((arr[i][0] == -2) || (arr[0][i] == -2)) dot_count++;
   }

   int c_f_d = arr[0][0];
   int c_b_d = arr[0][3];

   for(int i=1; i<4 && c_f_d != -2; i++)
   {
    if (arr[i][i] == c_f_d || arr[i][i] == -1 || c_f_d == -1) 
    {
        f_d++;
        c_f_d = (c_f_d==-1)?arr[i][i]:c_f_d;
    }
   }

   if(f_d == 4) return c_f_d;
   if (c_f_d == -2) dot_count += 1;

   for(int i=1; i<4 && c_b_d != -2; i++)
   {
    if (arr[i][3-i] == c_b_d || arr[i][3-i] == -1 || c_b_d == -1) 
    {
        b_d++;
        c_b_d = (c_b_d==-1)?arr[i][3-i]:c_b_d;
    }
   }
   
   if(b_d == 4) return c_b_d;
   if (c_b_d == -2) dot_count += 1;

   for (int i=1; i<4 && !dec_flag; i++) 
   {
       
        //compute the horizontal matches 
        for(int j=0; j<4 && !dec_flag; j++)
        {
            if (arr[i][j] == -2 || arr[i][j] == -2)   
            {
                dot_count++;
            }

            if ((h_curr[j] != -2) && (arr[j][i] == h_curr[j] || arr[j][i] == -1 || h_curr[j] == -1))
            {
                h_arr[j] += 1;
                h_curr[j] = (arr[j][i] == -1)?h_curr[j]:arr[j][i];
                if (h_arr[j] == 4)
                {
                    
                    won = h_curr[j];
                    dec_flag = 1;
                    continue;
                }
            }
            if ((v_curr[j] != -2)  && (arr[i][j] == v_curr[j] || arr[i][j] == -1 || v_curr[j] == -1))
            {
                v_arr[j] += 1;
                v_curr[j] = (arr[i][j] == -1)?v_curr[j]:arr[i][j];
                if (v_arr[j] == 4)
                {
                    won = v_curr[j];
                    dec_flag = 1;
                    continue;
                }
            }
        }
   }
    
   if (dec_flag) return won;
   else if(dot_count)   return -1;
   else return -2;
    
}

int main()
{
    
    int num_cases;
    int result;
    char c;
    int arr[4][4];
    cin>>num_cases;
    int count = 0;
    map<char, int> char_map;
    char_map['X'] = 1;
    char_map['O'] = 0;
    char_map['T'] = -1;
    char_map['.'] = -2;
    while (count < num_cases)
    {
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                cin>>c;
                arr[i][j] = char_map[c];
            }
        }
        result = computeResult(arr);
        cout<<"Case #"<<count+1<<": " ;
        switch(result)
        {
            case 0:
                    cout<<"O won"<<"\n";
                    break;
            case 1:
                    cout<<"X won"<<"\n";
                    break;
            case -1:
                    cout<<"Game has not completed"<<"\n";
                    break;
            case -2:
                    cout<<"Draw"<<"\n";
                    break;
                    
        }
        count++;
    }
}

