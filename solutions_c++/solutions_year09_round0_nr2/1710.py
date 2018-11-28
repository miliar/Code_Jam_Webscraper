#include <iostream>
#include <fstream>
#include <vector>
#include <map>

void radixSort(int *source, int *dest,
			   const int dataCount, unsigned int *data)
{
	int *tpm = (int*)malloc(sizeof(int)*dataCount);
	int *count = (int*)calloc(65536, sizeof(int));
	int *index = (int*)malloc(sizeof(int)*65536);
	
	for(int i=0;i< dataCount;i++){
		count[data[i] & 0xffff]++;
	}
	index[0] = 0;
	for(int i=1;i< 65536;i++){
		index[i] = index[i-1] + count[i-1];
	}
		if(source){
			for(int i=0;i< dataCount;i++){
				tpm[index[data[source[i]] & 0xffff]++] = source[i];
			}
		}else{
			for(int i=0;i< dataCount;i++){
				tpm[index[data[i] & 0xffff]++] = i;
			}
		}
	
	memset(count, 0, sizeof(int)*65536);
	for(int i=0;i< dataCount;i++){
		count[(data[i] >> 16) & 0xffff]++;
	}
	index[0] = 0;
	for(int i=1;i< 65536;i++){
		index[i] = index[i-1] + count[i-1];
	}

		for(int i=0;i< dataCount;i++){
			dest[index[(data[tpm[i]] >> 16) & 0xffff]++] = tpm[i];
		}
	
	free(tpm);
	free(count);
	free(index);
}


#define MAX_SIZE 102

#define APOS(h, w) (h*width)+w
#define NORTH(h, w) ((h-1)*width)+w
#define WEST(h, w) (h*width)+w-1
#define EAST(h, w) (h*width)+w+1
#define SOUTH(h, w) ((h+1)*width)+w

#define HH(pos) (pos/width)
#define WW(pos) (pos%width)

int height, width;

int *area;
int *drain1;
//int *drain2;
bool *inb;

void get(int pos, std::vector< int > &bas){
	if(!inb[pos]){
		bas.push_back(pos);
		inb[pos] = true;
	}
	if(drain1[pos] != -1){
		if(!inb[drain1[pos]])
			get(drain1[pos], bas);
	}
	int h = HH(pos);
	int w = WW(pos);
	if(h > 0){ // north
		if(drain1[NORTH(h, w)] == pos){
				get(NORTH(h, w), bas);
		}
	}
	if(w > 0){	// west
		if(drain1[WEST(h, w)] == pos){
				get(WEST(h, w), bas);
		}
	}
	if(w < width-1){ // east
		if(drain1[EAST(h, w)] == pos){
				get(EAST(h, w), bas);
		}
	}
	if(h < height-1){ // south
		if(drain1[SOUTH(h, w)] == pos){
				get(SOUTH(h, w), bas);
		}
	}
}
 
int main (int argc, char * const argv[]) {
//	std::ifstream ifile("input");
//	std::ifstream ifile("B-small-attempt0.in");
	std::ifstream ifile("B-large.in");
	std::ofstream ofile("output2");
	
	char buffer[1024];
	char *piece;

	int caseCount;
	ifile >>caseCount;

	area = (int*)malloc(sizeof(int)*MAX_SIZE*MAX_SIZE);
	int *basin = (int*)malloc(sizeof(int)*MAX_SIZE*MAX_SIZE);

	drain1 = (int*)malloc(sizeof(int)*MAX_SIZE*MAX_SIZE);
//	drain2 = (int*)malloc(sizeof(int)*MAX_SIZE*MAX_SIZE);

	inb = (bool*)malloc(sizeof(bool)*MAX_SIZE*MAX_SIZE); 

	int minatt, minpos;
	for(int i=1;i<= caseCount;i++){
		memset(basin, 0, sizeof(int)*MAX_SIZE*MAX_SIZE);
		memset(inb, 0, sizeof(int)*MAX_SIZE*MAX_SIZE);
		ifile >>height >>width;
		ifile.get();

		for(int j=0;j< height*width;j++){
			drain1[j] = -1;
		}
		
		for(int h=0;h< height;h++){
			ifile.getline(buffer, 1024);
//			std::cout<< "buffer: "<< buffer<< std::endl;
			piece = strtok(buffer, " \n");
			for(int w=0;w< width;w++){
				area[(h*width)+w] = atoi(piece);
//				std::cout<< area[(h*width)+w]<< " ";
				piece = strtok(NULL, " \n");
			}
//			std::cout<< std::endl;
		}

		for(int h=0;h< height;h++){
			for(int w=0;w< width;w++){
				minatt = area[APOS(h, w)];
				minpos = -1;
				// for every cell
				if(h > 0) // north
					if(area[NORTH(h, w)] < minatt){
						minatt = area[NORTH(h, w)];
						minpos = 0;
					}
				if(w > 0)	// west
					if(area[WEST(h, w)] < minatt){
						minatt = area[WEST(h, w)];
						minpos = 1;
					}
				if(w < width-1) // east
					if(area[EAST(h, w)] < minatt){
						minatt = area[EAST(h, w)];
						minpos = 2;
					}
				if(h < height-1) // south
					if(area[SOUTH(h, w)] < minatt){
						minatt = area[SOUTH(h, w)];
						minpos = 3;
					}
//				std::cout<< minpos<< std::endl;
				switch (minpos) {
					case -1:
						break;
					case 0:
						drain1[APOS(h, w)] = NORTH(h, w);	// 1
						break;
					case 1:
						drain1[APOS(h, w)] = WEST(h, w);
						break;
					case 2:
						drain1[APOS(h, w)] = EAST(h, w);
						break;
					case 3:
						drain1[APOS(h, w)] = SOUTH(h, w);
						break;

					default:
						assert(false);
						break;
				}
			}
		}

		int bCount = 0;
		std::map< int, std::vector< int > > bmap;
		for(int j=0;j< height*width;j++){
			if(!inb[j]){
				std::vector< int > b;
				get(j, b);
				bmap[bCount++] = b;
			}
		}

//		std::cout<< "bCount: "<< bCount<< std::endl;
		unsigned int *bsize = (unsigned int*)malloc(sizeof(unsigned int)*bCount);
		for(int b=0;b< bCount;b++){
			bsize[b] = bmap.size();
			for(int k=0;k< bmap[b].size();k++){
//				std::cout<< bmap[b][k]<< " ";
			}
//			std::cout<< std::endl;
		}

		int *pm = (int*)malloc(sizeof(int)*bCount);
		radixSort(NULL, pm, bCount, bsize);

		for(int b=0;b< bCount;b++){
//			std::vector< int > bv = bmap[pm[bCount-b-1]];
			std::vector< int > bv = bmap[pm[b]];
			for(int k=0;k< bv.size();k++){
				area[bv[k]] = 'a'+b;
			}
		}
		
		free(bsize);
		free(pm);
		std::cout<< "Case #"<< i<< ": "<< std::endl;
		for(int h=0;h< height;h++){
			for(int w=0;w< width;w++){
				std::cout<< (char)area[APOS(h, w)]<< " ";
			}
			std::cout<< std::endl;
		}

		ofile<< "Case #"<< i<< ": "<< std::endl;
		for(int h=0;h< height;h++){
			for(int w=0;w< width;w++){
				ofile<< (char)area[APOS(h, w)]<< " ";
			}
			ofile<< std::endl;
		}
	}

	free(area);
	free(basin);
	ifile.close();
	ofile.close();
    return 0;
}
