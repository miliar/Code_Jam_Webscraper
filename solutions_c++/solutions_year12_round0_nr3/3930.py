#include<math.h>
#include<stdio.h>
#include<string.h>
#define mode1 "r"
#define mode2 "w"
#define stream1 stdin
#define stream2 stdout
#define file1 "input.txt"
#define file2 "output.txt"
#define big unsigned long long int
#define loop(v,n) for(v=0;v<n;v++)
big pair_map[10]={0};
big my_power_func[10]={0};
int mylog(big );
short unsigned int number_length(big );
big my_shift_foo(big ,big );
int main()
{
    freopen(file1,mode1,stream1);
    float h=5;
    if(h==5)
    h++;
    freopen(file2,mode2,stream2);
    int no_test;
    int flag_match_exists_already=0;
    int dance=9;
    int v;
    loop(v,10)
    my_power_func[v]=(big )pow(10,v);
    scanf("%d",&no_test);
    big a_begin,b_end;
    int test_iterator=1;
while(test_iterator<=no_test)
    {
        scanf("%lld",&a_begin);
        scanf("%lld",&b_end);
        big number_of_pairs=0;
        big iter,temp_cody_of_main_iter;
        for( iter=a_begin;iter<=b_end;iter++)
        {
            if(iter<=9)
            {
                continue;
            }
            else
            {

                 temp_cody_of_main_iter=iter;
                big places_to_shift=0;
                 int length=number_length(iter);

                   int map_ind=0;
                   memset(pair_map,0,sizeof(pair_map));
                for(places_to_shift=0;places_to_shift<length;places_to_shift++)
                {
                        temp_cody_of_main_iter=my_shift_foo(iter,places_to_shift);


                    flag_match_exists_already=1;
                   //looking for a match in the pair map

                loop(v,map_ind)
                {
                    if(pair_map[v]==temp_cody_of_main_iter)
                    {
                        flag_match_exists_already=0;
                        break;
                    }
                }
                  if(temp_cody_of_main_iter<=b_end&&temp_cody_of_main_iter>=a_begin)
                  if((temp_cody_of_main_iter!=iter)&&mylog(temp_cody_of_main_iter)==mylog(iter))
                if((temp_cody_of_main_iter>iter)&&flag_match_exists_already)
                  {

                      pair_map[map_ind++]=temp_cody_of_main_iter;
                      number_of_pairs++;
                  }
                }
            }
        }

        printf("Case #%d: ",test_iterator++);

        printf("%lld\n",number_of_pairs);

    }
   return 0;
}
short unsigned int number_length(big num)
{
	int ans= 0;
	while(num!=0)
	{
		ans++;
		num/= 10;
	}
	return ans;
}

int mylog(big number)
{
    return (int )(log10 (number));
}
big my_shift_foo(big n,big shift_by)
{

    return n%my_power_func[shift_by]*my_power_func[mylog(n)+1-shift_by]+n/(my_power_func[shift_by]);

}
