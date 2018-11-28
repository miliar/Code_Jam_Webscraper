#include<iostream>
using namespace std;
int main()
{
    int case_num;
    int * results;

    cin >> case_num;
    bool flag = false;
    results = new int[case_num];
    for(int case_index =0;case_index < case_num; ++case_index)
    {
        int sq[4][4] = {0};
        int col_sum[4] = {0};
        char c;
        int tR=-1,tC=-1;
        int result = 0;
        int num = 0;
        flag = false;
        for(int i = 0;i < 4;i++)
        {
            int sum = 0;
            for(int j = 0; j < 4; j++)
            {
                cin >> c;
                if(flag)
                    continue;
                switch(c)
                {
                case 'X':
                    sq[i][j] = 1;
                    num ++;
                    break;
                case 'O':
                    sq[i][j] = -1;
                    num ++;
                    break;
                case '.':
                    sq[i][j]= 0;
                    break;
                case 'T':
                    sq[i][j]= 0;
                    tR = i;
                    tC = j;
                    break;
                }
                sum += sq[i][j];
                col_sum[j] += sq[i][j];
            }


           if(flag)
                continue;
            if(sum == 4 || (sum == 3 && i == tR) )
            {
                result = 1;
                flag = true;
                continue;
            }else if(sum == -4 || (sum == -3 && i == tR))
            {
                result = 2;
                flag = true;
                continue;
            }
        }
        if(result == 0)
        {
            for (int j = 0; j < 4; ++j)
            {

                if(col_sum[j] == 4 || (col_sum[j] == 3 && j ==  tC))
                {
                    result = 1;
                    break;;
                }else if(col_sum[j] == -4 || (col_sum[j] == -3 && j ==  tC))
                {
                    result = 2;
                    break;
                }

            }
        }

        if(result == 0)
        {
            int left_top = 0, right_top = 0;
            for (int i = 0; i < 4; ++i)
            {
                left_top += sq[i][i];
                right_top += sq[i][3-i];
            }
            if(left_top == 4
                || right_top == 4
                || (left_top == 3 && tC == tR)
                || (right_top == 3 && (tC + tR) == 3))
            {
                result = 1;
            }else if(left_top == -4
                || right_top == -4
                || (left_top == -3 && tC == tR)
                || (right_top == -3 && (tC + tR) == 3))
            {
                result = 2;
            }

        }
        if(result == 0)
        {
            if((num == 15 && tC != -1)||num == 16)
                result = 3;
        }

        results[case_index] = result;
    }

    for (int i = 0; i < case_num; ++i)
    {
        switch(results[i])
        {
        case 0:
            printf("Case #%d: Game has not completed\n", i+1);
            break;
        case 1:
            printf("Case #%d: X won\n", i + 1);
            break;
        case 2:
            printf("Case #%d: O won\n", i + 1);
            break;
        case 3:
            printf("Case #%d: Draw\n", i + 1);
            break;

        }
    }
    delete[] results;
    return 0;
}
