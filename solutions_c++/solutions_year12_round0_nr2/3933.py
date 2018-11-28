#include <fstream>
#include <iostream>

int main(int argc, char *argv[])
{
    if (argc!=2) {
        std::cout<<"Error"<<std::endl;
        return 1;
    }
    std::ifstream input(argv[1]);
    std::string file_out = argv[1];
    file_out += ".out";
    std::ofstream output(file_out.c_str());
    int nb_case;
    input >> nb_case;
    for(int i_case=0; i_case<nb_case; ++i_case) {
        int N, S, p;
        input >> N >> S >> p;
        int nb_max = 0;
        for(int i=0; i<N; ++i) {
            int score;
            input >> score;
            if (score>0) {
                int max_normal = (score-1)/3+1;
                if (max_normal>=p) {
                    ++nb_max;
                } else if (S>0) {
                    int max_exceptional = (score+1)/3+1;
                    if (max_exceptional>=p) {
                        ++nb_max;
                        --S;
                    }
                }
            }
        }
        if (p==0) {
            nb_max = N;
        }
        output<<"Case #"<<(i_case+1)<<": "<<nb_max<<std::endl;
    }
    if (input.fail() || !output.good()) {
        std::cout<<"File error"<<std::endl;
        return 1;
    }
    return 0;
}
