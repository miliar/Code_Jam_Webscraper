#include<iostream>

int main()
{
    int t;
    std::cin>>t;
    for(int i=0;i<t;i++){
        int n,k;
        std::cin>>n>>k;
        /*
         * 0 0 
         * 1 10
         * 2 01
         * 3 11
         * 4 001
         * 5 101
         *
         * */
        std::cout<<"Case #"<<(i+1)<<": ";
        if((k&((1<<n)-1))==((1<<n)-1))
        {
            std::cout<<"ON\n";
        }else{
            std::cout<<"OFF\n";
        }
    }
}
