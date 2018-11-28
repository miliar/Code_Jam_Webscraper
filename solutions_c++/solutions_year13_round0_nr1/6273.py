#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <sys/timeb.h>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <sys/timeb.h>
#include <math.h>

bool repeat(std::string line){
    if (line.length()==1 || line=="") {
        return true;
    }else{
        if (line.at(0)==line.at(line.length()-1)) {
            line.erase(0,1);
            line.erase(line.length()-1,1);
            return repeat(line);
        }else{
            return false;
        }
    }
}

int c_count(std::string sline){
    if (sline.find(".")==std::string::npos) {
        if (sline.find("O")==std::string::npos) {
            return 0;
        }else if (sline.find("X")==std::string::npos){
            return 1;
        }else{
            return 3;
        }
    }
    return 2;
}

void word_tokenize(std::string s, std::vector<std::string> *tokens) {
    std::istringstream s_stream(s);
    copy(std::istream_iterator<std::string>(s_stream),
         std::istream_iterator<std::string>(),
         std::back_inserter<std::vector<std::string> >(*tokens));
};

int main(){
    std::ifstream infile;
    std::string sline="";
    infile.open("test.txt");
    FILE *pfile;
    pfile=fopen("myfile.txt","w");
    int line=0;
    int n_case=0;
    int n_line=1;
    std::string one="....";
    std::string two="....";
    std::string three="....";
    std::string four="....";
    std::string cross1="....";
    std::string cross2="....";
    int end_game=0;
    int cc=0;
    int notc=0;
    while(!infile.eof()){
        getline(infile,sline);
        if (line==0) {
            n_case=atoi(sline.c_str());
        }else{
            if (sline=="") {
                //std::cout<<cross2<<std::endl;
                if (c_count(one)==0 && end_game==0) {
                    fprintf(pfile,"Case #%i: X won\n",n_line);
                    end_game=1;
                }else if(c_count(one)==1 && end_game==0){
                    fprintf(pfile,"Case #%i: O won\n",n_line);
                    end_game=1;
                }else if(c_count(one)==2 && end_game==0){
                    notc=1;
                }
                if (c_count(two)==0 && end_game==0) {
                    fprintf(pfile,"Case #%i: X won\n",n_line);
                    end_game=1;
                }else if(c_count(two)==1 && end_game==0){
                    fprintf(pfile,"Case #%i: O won\n",n_line);
                    end_game=1;
                }else if(c_count(two)==2 && end_game==0){
                    notc=1;
                }
                if (c_count(three)==0 && end_game==0) {
                    fprintf(pfile,"Case #%i: X won\n",n_line);
                    end_game=1;
                }else if(c_count(three)==1 && end_game==0){
                    fprintf(pfile,"Case #%i: O won\n",n_line);
                    end_game=1;
                }else if(c_count(three)==2 && end_game==0){
                    notc=1;
                }
                if (c_count(four)==0 && end_game==0) {
                    fprintf(pfile,"Case #%i: X won\n",n_line);
                    end_game=1;
                }else if(c_count(four)==1 && end_game==0){
                    fprintf(pfile,"Case #%i: O won\n",n_line);
                    end_game=1;
                }else if(c_count(four)==2 && end_game==0){
                    notc=1;
                }
                if (c_count(cross1)==0 && end_game==0) {
                    fprintf(pfile,"Case #%i: X won\n",n_line);
                    end_game=1;
                }else if(c_count(cross1)==1 && end_game==0){
                    fprintf(pfile,"Case #%i: O won\n",n_line);
                    end_game=1;
                }else if(c_count(cross1)==2 && end_game==0){
                    notc=1;
                }
                if (c_count(cross2)==0 && end_game==0) {
                    fprintf(pfile,"Case #%i: X won\n",n_line);
                    end_game=1;
                }else if(c_count(cross2)==1 && end_game==0){
                    fprintf(pfile,"Case #%i: O won\n",n_line);
                    end_game=1;
                }else if(c_count(cross2)==2 && end_game==0){
                    notc=1;
                }
                if (end_game==0 && notc==1) {
                    fprintf(pfile,"Case #%i: Game has not completed\n",n_line);
                }else if (end_game==0 && notc==0){
                    fprintf(pfile,"Case #%i: Draw\n",n_line);
                }
                n_line++;
                cc=0;
                std::string one="....";
                std::string two="....";
                std::string three="....";
                std::string four="....";
                std::string cross1="....";
                std::string cross2="....";
                end_game=0;
                notc=0;
            }
            else if (end_game==0) {
                //printf("cc is %i ",cc);
                //std::cout<<"line is "<<sline<<std::endl;
                one[cc-1]=sline[0];
                two[cc-1]=sline[1];
                three[cc-1]=sline[2];
                four[cc-1]=sline[3];
                cross1[cc-1]=sline[cc-1];
                cross2[4-cc]=sline[4-cc];
                if (sline.find(".")==std::string::npos) {
                    if (sline.find("O")==std::string::npos) {
                        fprintf(pfile,"Case #%i: X won\n",n_line);
                        //printf("here1!\n");
                        //std::cout<<sline<<std::endl;
                        end_game=1;
                    }else if (sline.find("X")==std::string::npos){
                        fprintf(pfile,"Case #%i: O won\n",n_line);
                        end_game=1;
                    }
                }
            }
            
        }
        cc++;
        line++;
    }
    fclose(pfile);
    
}