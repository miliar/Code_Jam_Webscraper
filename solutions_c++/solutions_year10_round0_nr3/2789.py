#include<iostream>

using namespace std;

main()
{
    freopen( "C-small-attempt0.in", "r", stdin );
    freopen( "C-small-attempt0.out", "w", stdout );
    int Cases;
    cin>>Cases;
    for( int i = 0; i < Cases; ++i )
    {
        int firstIndex, lastIndex;
        long int capacity, time, noGroups, groupElements[30], matrix[30][100], money[100], totalMoney[101];
        totalMoney[0] = 0;
        cin>>time;
        cin>>capacity;
        cin>>noGroups;
        for( int j = 0; j <  noGroups; ++j )
            cin>>groupElements[j];
        int ptr = 0;
        int sum;
        int ctr = 0;
        bool flag = false;
        do
        {
            sum = 0;
            int k;
            for( k = 0; k < noGroups; ++k )
            {
                int tempSum = sum + groupElements[ptr];
                if( tempSum <= capacity )
                {
                    sum = tempSum;
                    matrix[ctr][k] = groupElements[ptr];
                }
                else
                    break;
                ptr++;
                if( ptr == noGroups )
                    ptr = 0;
            }
            money[ctr] = sum;
            totalMoney[ctr + 1] = totalMoney[ctr] + money[ctr];
            int tempPtr = ptr;
            for( ;k < noGroups; ++k )
            {
                matrix[ctr][k] = groupElements[tempPtr++];
                if( tempPtr == noGroups )
                    tempPtr = 0;
            }
            /*cout<<money[ctr]<<" ";
            for( k = 0; k < noGroups; ++k )
            {
                cout<<matrix[ctr][k]<<" ";
            }
            cout<<endl;*/
            for( k = 0; k < ctr; ++k )
            {
                flag = true;
                for( int j = 0; j < noGroups && flag; ++j )
                    if( matrix[k][j] != matrix[ctr][j] )
                        flag = false;
                if( flag )
                {
                    firstIndex = k;
                    lastIndex = ctr;
                    break;
                }
            }
            ctr++;
        }while( !flag );
        //cout<<firstIndex<<" "<<lastIndex<<endl;
        long int final2 = 0, remMoney[101];
        long int time1, time2;
        if( time <= ctr )
        {
            time1 = time;
            time2 = 0;
        }
        else
        {
            time1 = ctr;
            time2 = time - ctr;
        }
        final2 = totalMoney[time1];
        //cout<<time1<<" "<<time2<<" "<<final2<<" ";
        int div = time2 / ( lastIndex - firstIndex );
        int rem = time2 - div * ( lastIndex - firstIndex );
        int ind2 = firstIndex + 1;
        //final2 = final2 + totalMoney[ctr] * div;
        remMoney[0] = 0;
        int k;
        for( k = 1; k <= ( lastIndex - firstIndex ); ++k )
        {
            remMoney[k] = remMoney[k-1] + money[ind2];
            ind2++;
        }
        final2 = final2 + remMoney[k-1] * div + remMoney[rem];
        cout<<"Case #"<<i+1<<": "<<final2<<endl;

    }
}
