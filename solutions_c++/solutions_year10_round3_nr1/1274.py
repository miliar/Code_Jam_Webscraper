#include <stdio.h>
#include <stdlib.h>

#include <map>

struct line_t
{
    line_t(int left_w,int right_w) : left_window(left_w), right_window(right_w) {}
    int left_window;
    int right_window;
};


int main ( void )
{
    int TEST_CASES;
    int N;

    std::map<int,line_t> left_up;
    std::map<int,line_t> right_up;

    int test_i;
    int number_i;

    if ( 1 != scanf ( "%d", &TEST_CASES )  )
    {
        printf ("wrong input\n" );
        return -1;
    }
    //printf ("%d\n", TEST_CASES );
    for ( test_i = 0; test_i < TEST_CASES; test_i++ )
    {
        if ( 1 != scanf ( "%d", &N ) )
        {
            printf ("wrong input 2\n" );
            return -1;
        }

        //printf ("%d\n", N );
        // load all the numbers insertion sort on the way
        for ( number_i = 0; number_i <N; number_i++ )
        {
            int left_w, right_w;
            if ( 2 != scanf ( "%d %d", &left_w, &right_w ) )
            {
                printf ("wrong input 3\n" );
                return -1;
            }
            if ( left_w < right_w )
            {
                left_up.insert(std::pair<int,line_t>(left_w,line_t(left_w,right_w) ) );
            }
            else
            {
                right_up.insert(std::pair<int,line_t>(right_w,line_t(left_w,right_w) ) );
            }
        }

        std::map<int,line_t>::iterator left_iter = left_up.begin();
//        while ( left_iter != left_up.end() )
//        {
//            printf ("%d %d\n", left_iter->second.left_window, left_iter->second.right_window );
//            ++left_iter;
//        }

        std::map<int,line_t>::iterator right_iter = right_up.begin();
//        while ( right_iter != right_up.end() )
//        {
//            printf ("%d %d\n", right_iter->second.left_window, right_iter->second.right_window );
//            ++right_iter;
//        }

        unsigned long crosses = 0;

        left_iter = left_up.begin();
        while ( left_iter != left_up.end() )
        {
            std::map<int,line_t>::iterator left_inner_iter = left_up.begin();
            while ( left_inner_iter != left_up.end() ) 
            {
                if ( left_inner_iter->second.left_window > left_iter->second.right_window ) break;
                if ( left_inner_iter->second.left_window < left_iter->second.left_window &&
                     left_inner_iter->second.right_window > left_iter->second.right_window ) crosses++;
                if ( left_inner_iter->second.left_window > left_iter->second.left_window &&
                     left_inner_iter->second.right_window < left_iter->second.right_window ) crosses++;
                ++left_inner_iter;
            }
            std::map<int,line_t>::iterator right_inner_iter = right_up.begin();
            while ( right_inner_iter != right_up.end() ) 
            {
                if ( right_inner_iter->second.right_window > left_iter->second.right_window ) break;
                if ( right_inner_iter->second.left_window > left_iter->second.left_window ) crosses++;
                ++right_inner_iter;
            }
            ++left_iter;
        }

        right_iter = right_up.begin();
        while ( right_iter != right_up.end() )
        {
            std::map<int,line_t>::iterator right_inner_iter = right_up.begin();
            while ( right_inner_iter != right_up.end() ) 
            {
                if ( right_inner_iter->second.right_window > right_iter->second.left_window ) break;
                if ( right_inner_iter->second.right_window < right_iter->second.right_window &&
                     right_inner_iter->second.left_window > right_iter->second.left_window ) crosses++;
                if ( right_inner_iter->second.right_window > right_iter->second.right_window &&
                     right_inner_iter->second.left_window < right_iter->second.left_window ) crosses++;
                ++right_inner_iter;
            }
            std::map<int,line_t>::iterator left_inner_iter = left_up.begin();
            while ( left_inner_iter != left_up.end() ) 
            {
                if ( left_inner_iter->second.left_window > right_iter->second.left_window ) break;
                if ( left_inner_iter->second.right_window > right_iter->second.right_window ) crosses++;
                ++left_inner_iter;
            }
            ++right_iter;
        }
        
        crosses = crosses / 2; 

        printf ("Case #%d: %lu\n", test_i + 1, crosses );


        left_up.clear();
        right_up.clear();
    }
}



