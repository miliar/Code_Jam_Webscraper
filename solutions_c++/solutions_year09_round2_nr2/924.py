#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);

    int T, i, j, len;
    char number[25];

    int X = 0;

    scanf("%d", &T);
    while (T--)
    {
        scanf("%s", number);
        len = strlen(number);
        for(i=len-1; i>0; --i)
        {
            if(number[i] > number[i-1]){
                break;
            }
        }

        if(i>0){
            for(j=len-1; j>i; --j){
                if(number[j] > number[i-1]) break;
            }

            char ch = number[j];
            number[j] = number[i-1];
            number[i-1] = ch;

            sort(number + i, number+len);
        } else {
            sort(number, number + len);

            for(j=len-1; j>0; --j){
                number[j+1] = number[j];
            }
            number[1] = '0';
            number[len+1] = '\0';

            if(number[0] == '0') {
                for(j=1; j<=len; ++j){
                    if(number[j] != '0'){
                        number[0] = number[j];
                        number[j] = '0';
                        break;
                    }
                }
            }
        }

        printf("Case #%d: %s\n", ++X, number);
    }

    fclose(stdin);
	fclose(stdout);

    return 0;
}
