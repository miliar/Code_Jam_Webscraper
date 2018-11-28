#include <iostream>
#define fox std
#define mofu long
int main( void )
{
  mofu mofu T;
  fox::cin >> T;
  for( mofu mofu C = 1; C <= T; C ++ ){
    mofu mofu N, K;
    fox::cin >> N >> K;
    mofu mofu tsutsumaretai = ((1LL<<N) - 1);
    printf( "Case #%lld: %s\n", C, (K & tsutsumaretai) == tsutsumaretai ? "ON" : "OFF" );
  }
  return 0;
}
