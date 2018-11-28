#include <cstdio>

int main(int argc, char* argv[])
{
        FILE *fp = fopen(*(argv+1), "r");
        int case_n;
        int pos[19];
        char data[600];
        char trun_data[600];
        int trun_len[500];
        char string[20] = "welcome to code jam";
        fscanf(fp, "%d", &case_n);
        fgets(data, 600,fp);
        for(int i = 0;i < case_n; i++)
        {
                int result = 0;
                fgets(data, 600, fp);
                char *data_ptr = data;
                char ch = 'q';
                int count = 0;
                int trun_size = 0;
                printf("Case #%d: ", i+1);
                while(*data_ptr != '\0')
                {
                        if(*data_ptr != 'w' &&
                        *data_ptr != 'e' &&
                        *data_ptr != 'l' &&
                        *data_ptr != 'c' &&
                        *data_ptr != 'o' &&
                        *data_ptr != 'm' &&
                        *data_ptr != ' ' &&
						*data_ptr != 't' &&
                        *data_ptr != 'd' &&
                        *data_ptr != 'j' &&
                        *data_ptr != 'a' &&
                        *data_ptr != 'm'){data_ptr++;}
                        else
                        {
                                if(*data_ptr != ch)
                                {
                                        if(count != 0)
                                        {
                                                trun_data[trun_size] = ch;
                                                trun_len[trun_size] = count;
                                                trun_size++;
                                        }
                                        //output here
                                        ch = *data_ptr;
                                        count = 1;
                                }
                                else
                                {
                                        count++;
                                }
                                data_ptr++;
                        }
                }
                if(ch != 'q')
                {
                        trun_data[trun_size] = ch;
                        trun_len[trun_size] = count;
                        trun_size++;
                }
                if(trun_size < 19)
                {
                        printf("0000");
                }
                else
                {
                        count = 0;
                        int data_pos = 0;
                        while(1)
                        {
                                if(trun_data[data_pos] == string[count])
                                {
                                        pos[count] = data_pos;
                                        if(count == 18)
                                        {
                                                int temp_res = 1;
                                                for(int counter1 = 0; counter1 < 19; counter1++)
                                                {
                                                        temp_res *= trun_len[pos[counter1]];
                                                }
                                                result = (result + temp_res%10000)%10000;
                                        }
                                        else
                                        {
                                                count++;
                                        }
                                }
                                data_pos++;
                                if(data_pos >= trun_size)
                                {
                                        count--;
                                        if(count == -1)
                                        {
                                                break;
                                        }
                                        data_pos = pos[count]+1;
                                }
                        }
						printf("%04d", result);
                }
                printf("\n");
        }
}
