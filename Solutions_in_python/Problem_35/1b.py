import string

class GraphNode(object):
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.flows_to = None
        self.flows_from = []
        self.label = None
    
    def set_flows_to(self, other):
        assert self.flows_to != other
        self.flows_to = other
        other.flows_from.append(self)
    
        

def label_node(node, label):
    if node.label is None:
        node.label = label
        if node.flows_to:
            label_node(node.flows_to, label)
                
        for from_node in node.flows_from:
            label_node(from_node, label)
    else:
        if node.label != label:
            print "Relabeling of node"
            adsafa


def label_nodes(h, w, node_map):
    current_label = 0
    for i in xrange(h):
        for j in xrange(w):
            label = string.lowercase[current_label]
            node = node_map[i][j]
            if node.label is None:
                label_node(node, label)
                current_label += 1
                
                
def flow_water(w,h, height_map, node_map):
    for i in xrange(h):
        for j in xrange(w):
            lowest = height_map[i][j]
            flow_to = None
            
            if i - 1 >= 0:
                if height_map[i-1][j] < lowest:
                    lowest = height_map[i-1][j]
                    flow_to = node_map[i-1][j]
            
            if j - 1 >= 0:
                if height_map[i][j-1] < lowest:
                    lowest = height_map[i][j-1]
                    flow_to = node_map[i][j-1]
                
            if j + 1 < w:
                if height_map[i][j+1] < lowest:
                    lowest = height_map[i][j+1]
                    flow_to = node_map[i][j+1]
                    
            if i + 1 < h:                    
                if height_map[i+1][j] < lowest:
                    lowest = height_map[i+1][j]
                    flow_to = node_map[i+1][j]
            
            if flow_to is not None:
                node_map[i][j].set_flows_to(flow_to)
            
        
def main():        
    number_of_cases = int(raw_input())
    for case_number in range(1, number_of_cases+1):
        h,w = map(int, raw_input().split())
        print 'Case #%d:' % (case_number,)
        height_map = []
        node_map  = []
        for i in xrange(h):
            height_map.append(raw_input().split())
            
            line = []
            for j in xrange(w):
                line.append(GraphNode(i,j))
                
            node_map.append(line)
        
        flow_water(w, h, height_map, node_map)
        label_nodes(h, w, node_map)
        
        for node_line in node_map:
            for node in node_line:
                print node.label,
            print
main()

#w, h = 3,3
#height_map = []
#node_map  = []

#height_map.append([9,6,3])
#height_map.append([5,9,6]) 
#height_map.append([3,5,9])
    
#for i in xrange(h):
    #line = []
    #for j in xrange(w):
        #line.append(GraphNode(i,j))
    
    #node_map.append(line)

#flow_water(w, h, height_map, node_map)
#label_nodes(h, w, node_map)


#for node_line in node_map:
    #for node in node_line:
        #print node.label,
    #print
        ##if node.flows_to:
            ##print node.x_pos, node.y_pos, node.flows_to.x_pos, node.flows_to.y_pos, node.label
        ##else:
            ##print node.x_pos, node.y_pos, -1, -1, node.label