import sys,copy

class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.sink = v  
    self.capacity = w
  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.sink, self.capacity)

class FlowNetwork(object):
  def __init__(self):
    self.adj = {}
    self.flow = {}
  
  def add_vertex(self, vertex):
    self.adj[vertex] = []
  
  def get_edges(self, v):
    return self.adj[v]
  
  def add_edge(self, u, v, w=0, x=0):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u,v,w)
    redge = Edge(v,u,x)
    edge.redge = redge
    redge.redge = edge
    self.adj[u].append(edge)
    self.adj[v].append(redge)
    self.flow[edge] = 0
    self.flow[redge] = 0
  
  # "Edmonds-Karp"
  def find_path_EK(self, source, sink):
    assert source!=sink
    back={}
    qu=[source];q0=0
    while q0<len(qu):
      u=qu[q0];q0+=1
      for e in self.get_edges(u):
        v=e.sink
        if v not in back:
          resid = e.capacity - self.flow[e]
          if resid>0:
            back[v]=e
            if v==sink:
              edges=[]
              while v!=source: e=back[v];edges.append(e);v=e.source
              edges.reverse()
              return edges
            qu.append(v)
    return None
  
  def max_flow_EK(self, source, sink):
    while 1:
      path = self.find_path_EK(source, sink)
      if not path:
        return sum(self.flow[edge] for edge in self.get_edges(source))
      flow=min([e.capacity-self.flow[e] for e in path])
      for e in path: self.flow[e]+=flow;self.flow[e.redge]-=flow
      #print "Increasing by",flow,"to",sum(self.flow[edge] for edge in self.get_edges(source))
      #self.prvflow()
  
  def find_path_Dinic(self,source,sink,ok):
    if source==sink: return []
    for e in self.get_edges(source):
      if e in ok and ok[e]==1 and self.flow[e]<e.capacity:
        p=self.find_path_Dinic(e.sink,sink,ok)
        if p!=None: return [e]+p
        ok[e]=0
    return None

  # Simple Dinic
  def max_flow_Dinic(self, source, sink):
    assert source!=sink
    while 1:
      lev={};ok={}
      qu=[source];q0=0;lev[source]=0
      while q0<len(qu):
        u=qu[q0];q0+=1
        for e in self.get_edges(u):
          v=e.sink
          if v not in lev:
            resid=e.capacity-self.flow[e]
            if resid>0: lev[v]=lev[u]+1;qu.append(v);ok[e]=1
      if sink not in lev: break
      while 1:
        path=self.find_path_Dinic(source,sink,ok)
        if not path: break
        flow=min([e.capacity-self.flow[e] for e in path])
        for e in path: self.flow[e]+=flow;self.flow[e.redge]-=flow
        #break# variation
    return sum(self.flow[e] for e in self.get_edges(source))
  
  def prvertices(self):
    for v in self.adj: print v
  
  def predges(self):
    for e in self.flow: print e
  
  def pradj(self):
    for v in self.adj:
      print v,":",
      for e in self.adj[v]: print e.sink,
      print
  
  def preflow(self):
    for e in self.flow: print "%s->%s:%s/%s"%(e.source,e.sink,self.flow[e],e.capacity)
  
  def prvflow(self,all=0):
    for v in self.adj:
      m=max([self.flow[e] for e in self.adj[v]])
      if m>0 or all:
        print v,":",
        for e in self.adj[v]:
          if self.flow[e]>0 or all: print "%s:%s/%s"%(e.sink,self.flow[e],e.capacity),
        print

def thingold(N,sentences):
  g=FlowNetwork()
  words={}
  for i,S in enumerate(sentences):
    for w in S: words[w]=1
    g.add_vertex(i)
  for w in words:
    g.add_vertex('IN'+w)
    g.add_vertex('OUT'+w)
    g.add_edge('IN'+w,'OUT'+w,1)
  for i,S in enumerate(sentences):
    for w in S:
      if i!=1: g.add_edge(i,'IN'+w,1)
      if i!=0: g.add_edge('OUT'+w,i,1)
  return g.max_flow_EK(0,1)

def thing(N,M,prepl):
  board0=[[0]*N for i in range(N)]
  # x=1, +=2, o=3
  # bit0 = rooks, bit1 = bishops
  dec='.x+o'
  for p in prepl:
    v=dec.find(p[0])
    r=int(p[1])-1
    c=int(p[2])-1
    board0[r][c]=v
  board=copy.deepcopy(board0)

  # Rooks
  occrow=[0]*N;occcol=[0]*N
  for r in range(N):
    for c in range(N):
      if board0[r][c]&1: occrow[r]=1;occcol[c]=1
  freerows=[];freecols=[]
  for i in range(N):
    if occrow[i]==0: freerows.append(i)
    if occcol[i]==0: freecols.append(i)
  assert len(freerows)==len(freecols)
  for (r,c) in zip(freerows,freecols): board[r][c]|=1

  # Bishops
  # Label diagonals by (leading) r-c and (lagging) r+c
  occlead={};occlagg={}
  for r in range(N):
    for c in range(N):
      if board[r][c]&2: occlead[r-c]=1;occlagg[r+c]=1
  g=FlowNetwork()
  g.add_vertex('SOURCE')
  g.add_vertex('SINK')
  freelead={};freelagg={}
  for r in range(N):
    for c in range(N):
      if r-c not in occlead and r+c not in occlagg:
        assert (board[r][c]&2)==0
        leadv='LEAD%d'%(r-c)
        laggv='LAGG%d'%(r+c)
        if r-c not in freelead:
          freelead[r-c]=1
          g.add_vertex(leadv)
          g.add_edge('SOURCE',leadv,1)
        if r+c not in freelagg:
          freelagg[r+c]=1
          g.add_vertex(laggv)
          g.add_edge(laggv,'SINK',1)
        g.add_edge(leadv,laggv,1)
  maxf=g.max_flow_EK('SOURCE','SINK')
  #print maxf
  for e in g.flow:
    if e.source[:4]=='LEAD' and e.sink[:4]=='LAGG' and g.flow[e]==1:
      #print e.source,e.sink
      lead=int(e.source[4:])
      lagg=int(e.sink[4:])
      assert (lead&1)==(lagg&1)
      r=(lagg+lead)/2;c=(lagg-lead)/2
      assert r>=0 and r<N and c>=0 and c<N
      board[r][c]|=2
  #g.preflow()

  # Output
  y=0;z=0
  for r in range(N):
    for c in range(N):
      b=board[r][c]
      y+=(b&1)+(b>>1&1)
      z+=(b!=board0[r][c])
  print y,z
  for r in range(N):
    for c in range(N):
      b=board[r][c]
      if b!=board0[r][c]: print dec[b],r+1,c+1

T=int(sys.stdin.readline())
for case in range(1,T+1):
  [N,M]=[int(y) for y in sys.stdin.readline().strip().split()]
  prepl=[]
  for i in range(M):
    prepl.append(sys.stdin.readline().strip().split())
  print "Case #%d:"%case,;thing(N,M,prepl)
