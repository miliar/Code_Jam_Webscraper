#include<cstdio>
#include<cstdlib>
#define SIZE 110

struct bot{
       int curr_pos;
       int next_pos[SIZE];
       int index;
       int total_next_pos;
       };

bot b,o;

int main()
{
    FILE* bot_inp = fopen("d:\\bot_inp.txt","r");
    FILE* bot_trust = fopen("d:\\bot_trust.txt","w");
    
    int test_cases,t;
    int num;
    char bot;
    int arr[SIZE],count=0,curr_case=1;    
    
    fscanf(bot_inp,"%d",&test_cases);
    //fflush(bot_inp);
    
    while(test_cases--)
    {
        fscanf(bot_inp,"%d",&num);                                 //Number of elements in sequence
        count = 0;                                                //Count of total elements in input sequence
        b.curr_pos=o.curr_pos=1;                                  //Reset curr_position
        b.index=o.index=0;                                        //Reset index of next position
        b.total_next_pos = o.total_next_pos = 0;
        t=0;
        char ch;
        //read input sequence
        for(int i=0;i<num;i++)
        {
            while((ch=fgetc(bot_inp))==' ')
            ;
            ungetc(ch,bot_inp);
            fscanf(bot_inp,"%c",&bot);
            if(bot=='B')
            {
              while((ch=fgetc(bot_inp))==' ')
              ;
              ungetc(ch,bot_inp);
              fscanf(bot_inp,"%d",&b.next_pos[b.total_next_pos++]);
              arr[count++]='b';
            }
            else if(bot=='O')
            {
              while((ch=fgetc(bot_inp))==' ')
              ;
              ungetc(ch,bot_inp);
              fscanf(bot_inp,"%d",&o.next_pos[o.total_next_pos++]);
              arr[count++]='o';
            }
        }
        //read sequence ended

        if(b.total_next_pos==0 && o.total_next_pos==0)
        {
             fprintf(bot_trust,"Case #%d: ",curr_case);
             fprintf(bot_trust,"0\n");
             fflush(bot_trust);
             curr_case++;

        }
        else if(b.total_next_pos==0) // #1
        {
             t = o.next_pos[0]-1;
             t++;
             o.curr_pos=o.next_pos[0];
             
             for(int j=1;j<o.total_next_pos;j++)
             {
                     t += abs(o.next_pos[j]-o.curr_pos);
                     t++;
                     o.curr_pos=o.next_pos[j];
             }
             
             fprintf(bot_trust,"Case #%d: ",curr_case);
             fprintf(bot_trust,"%d\n",t);
             fflush(bot_trust);
             curr_case++;

             
        } // else #1 ended
        else if(o.total_next_pos==0) // #2
        {
             t = b.next_pos[0]-1;
             t++;
             b.curr_pos=b.next_pos[0];
             
             for(int j=1;j<b.total_next_pos;j++)
             {
                     t += abs(b.next_pos[j]-b.curr_pos);
                     t++;
                     b.curr_pos=b.next_pos[j];
             }
             
             fprintf(bot_trust,"Case #%d: ",curr_case);
             fprintf(bot_trust,"%d\n",t);
             fflush(bot_trust);
             curr_case++;

             
        } //else #2 ended
        else     // #3
        {
            int ind=0;
            
            while(ind!=count)
            {
            if(arr[ind]=='o') 
            {
                 while(1)
                 {
                     t++;
                     
                     int diff2 = b.next_pos[b.index] - b.curr_pos ;
             
                     if(diff2 > 0)
                     {
                              b.curr_pos++;
             
                     }
                     else if(diff2 < 0)
                     {
                              b.curr_pos--;
             
                     }
                     int diff1 = o.next_pos[o.index] - o.curr_pos ;
             
                     if(diff1 > 0)
                     {
                              o.curr_pos++;
             
                     }
                     else if(diff1 < 0)
                     {
                              o.curr_pos--;
             
                     }
                     else
                     {
                         o.index++;
                         ind++;
                         break;
                     }
                 }//while(1) ended
            }     //if(arr[ind]=='o') ended
            else  // #3(i)
            {
                while(1)
                 {
                     t++;
                     
                     int diff2 = o.next_pos[o.index] - o.curr_pos ;
                     if(diff2 > 0)
                     o.curr_pos++;
                     else if(diff2 < 0)
                     o.curr_pos--;
                     
                     int diff1 = b.next_pos[b.index] - b.curr_pos ;
                     if(diff1 > 0)
                     b.curr_pos++;
                     else if(diff1 < 0)
                     b.curr_pos--;
                     else
                     {
                         b.index++;
                         ind++;
                         break;
                     }
                 }//while(1) ended
            }//else #3(i) ended
        }//while(ind!=count) ended
        fprintf(bot_trust,"Case #%d: ",curr_case);
        fprintf(bot_trust,"%d\n",t);
        fflush(bot_trust);
        curr_case++;

    }//else #3 ended
}//while(test_cases--) ended
}//int main() ended
