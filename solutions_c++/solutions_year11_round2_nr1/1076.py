#include <iostream>
#include <iomanip>
#include <vector>


int main(){
    unsigned T;
    std::cin >> T;
    for(unsigned t=1; t<=T; ++t){
        std::cout << "Case #" << t << ":" << std::endl;
        unsigned N;
        std::cin >> N;
        std::vector<std::vector<char> > res(N, std::vector<char>(N));
        std::cin.ignore(42, '\n');
        for(unsigned i=0; i<N; ++i){
            for(unsigned j=0; j<N; ++j)
                res[i][j]=std::cin.get();
            std::cin.ignore(42, '\n');
        }

        std::vector<double> WP(N, 0);
        std::vector<unsigned> played(N, 0);
        for(unsigned i=0; i<N; ++i){
            for(unsigned j=0; j<N; ++j)
                if(res[i][j]!='.'){
                    played[i]++;
                    if(res[i][j]=='1')
                        WP[i]++;
                }
            WP[i]/=played[i];
        }

        std::vector<double> OWP(N, 0);
        for(unsigned i=0; i<N; ++i){
            for(unsigned j=0; j<N; ++j)
                if(res[i][j]!='.'){
                    unsigned won = res[j][i]-'0';
                    OWP[i]+=(WP[j]*played[j]-won)/(played[j]-1);
                }
            OWP[i]/=played[i];
        }

        std::vector<double> OOWP(N, 0);
        for(unsigned i=0; i<N; ++i){
            for(unsigned j=0; j<N; ++j)
                OOWP[i]+=res[i][j]=='.'?0:OWP[j];
            OOWP[i]/=played[i];
        }

        for(unsigned i=0; i<N; ++i)
            std::cout << std::setprecision(8) << 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] << std::endl;
    }
}
