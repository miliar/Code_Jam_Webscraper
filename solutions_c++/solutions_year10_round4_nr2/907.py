#include <stdio.h>
int P,M[1024];
int numTicket;
void binary(int start,int end)
{
    for( int i = start ; i <= end ; i++ )
    {
        if( M[i] < P )
        {
            for( int j = start ; j <= end ; j++ )
                M[j]++;
            numTicket++;
            break;
        }
    }
    for( int i = start ; i <= (start+end)/2 ; i++ )
    {
        if( M[i] < P )
        {
            binary(start,(start+end)/2);
            break;
        }
    }
    for( int i = (start+end+1)/2 ; i <= end ; i++ )
    {
        if( M[i] < P )
        {
            binary((start+end+1)/2,end);
            break;
        }
    }
}
int main()
{
    int tmp,T,numTeam;
    scanf("%d",&T);
    for( int i = 0 ; i < T ; i++ )
    {
        scanf("%d",&P);
        numTeam = 1;
        for( int j = 0 ; j < P ; j++ )
            numTeam *= 2;
        for( int j = 0 ; j < numTeam ; j++ )
            scanf("%d",&M[j]);
        for( int j = 1 ; j < numTeam ; j++ )
            scanf("%d",&tmp);
        numTicket = 0;
        binary(0,numTeam-1);
        printf("Case #%d: %d\n",i+1,numTicket);
    }
    return 0;    
}
