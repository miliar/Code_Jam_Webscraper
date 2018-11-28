
//#define BEFORE_SUBMIT

#ifdef BEFORE_SUBMIT
    #include <conio.h>
#endif /* BEFORE_SUBMIT */
    #include <iostream>
    #include <cmath>
    
    
    
    using namespace std;

/*
Small dataset

1 ? N ? 10;
0 ? K ? 100; 


1 ? N ? 30;
0 ? K ? 108; 

*/

    int main()
    {
        int no_of_test_cases;
        cin>>no_of_test_cases;
        int temp1 = no_of_test_cases;
        
        while (temp1--)
        {
            long long int N, K, power_n, mod_val;
            cin>>N;
            cin>>K;
            if (K<N)
            {
                cout<<"Case #"<<no_of_test_cases-temp1<<": OFF\n";       
                continue;
            }
            /* K%(2^N)*/
            power_n = pow((long double)2, (long double)N);
            mod_val = K%power_n;
            if (mod_val == power_n-1)
            {
                cout<<"Case #"<<no_of_test_cases-temp1<<": ON\n";           
            }
            else
            {
                cout<<"Case #"<<no_of_test_cases-temp1<<": OFF\n";
            }
        }
#ifdef BEFORE_SUBMIT
        getch();
#endif /* BEFORE_SUBMIT */
        return 0;
    }
