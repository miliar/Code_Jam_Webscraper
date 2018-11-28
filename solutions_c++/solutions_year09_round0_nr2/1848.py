#include <iostream>
#include <cstdio>
#include <map>

#define MAX_ALT 10000
#define N 0
#define W 1
#define E 2
#define S 3

struct MapNode {
  int maxw, maxh;
  int w, h;
  MapNode *drainmap;

  bool calcd;
  int calcd_id;
  int alt;

  int id;

  MapNode() { calcd = false; }

  int get_drain_id() {
    if(calcd) return calcd_id;
    
    MapNode *nghbrs[4] = {0};

    if(h) nghbrs[N] = &drainmap[(h-1)*maxw + w];
    if(w) nghbrs[W] = &drainmap[h*maxw + (w-1)];
    if(w < (maxw-1)) nghbrs[E] = &drainmap[h*maxw + (w+1)];
    if(h < (maxh-1)) nghbrs[S] = &drainmap[(h+1)*maxw + w];

    calcd = true;

    MapNode *best = NULL;

    for(int i=0; i<4; i++)
      if(nghbrs[i] && nghbrs[i]->alt < alt) {
	if(!best) best = nghbrs[i];
	else if((alt - nghbrs[i]->alt) > (alt - best->alt)) best = nghbrs[i];
      }

    if(best) return calcd_id = best->get_drain_id();
    else return calcd_id = id;
  }
};

void process_map() {
  int h, w;
  std::cin >> h;
  std::cin >> w;

  MapNode drainmap[h*w];

  for(int y=0; y<h; y++)
    for(int x=0; x<w; x++) {
      drainmap[y*w + x].w = x;
      drainmap[y*w + x].h = y;

      drainmap[y*w + x].maxw = w;
      drainmap[y*w + x].maxh = h;

      drainmap[y*w + x].drainmap = drainmap;

      std::cin >> drainmap[y*w + x].alt;
      drainmap[y*w + x].id = y*w + x;
    }

  char cur_letter = 'a';
  typedef std::map<int, char> TranslationMap;
  TranslationMap translation;
  
  for(int y=0; y<h; y++) {
    for(int x=0; x<w; x++) {
      int alt = drainmap[y*w + x].get_drain_id();
      char c;

      TranslationMap::iterator i = translation.find(alt);

      if(i == translation.end()) {
	translation[alt] = cur_letter;
	c = cur_letter++;
      }

      else c = i->second;

      printf("%c", c);
      if(x != (w-1)) printf(" ");
    }

    printf("\n");
  }
}

int main() {
  int maps;
  std::cin >> maps;

  for(int i=0; i<maps; i++) {
    printf("Case #%d:\n", i+1);
    process_map();
  }
}
